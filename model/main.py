import os
import pytesseract
import pandas as pd
import torch
import numpy as np
from transformers import LayoutLMForSequenceClassification, LayoutLMTokenizer
from PIL import Image
from pdf2image import convert_from_path
from datasets import Dataset
from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = api_key


pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

classes = ['invoice', 'resume', 'passport', 'Tax_Statement',
           'balance_sheet', 'Income_Statement', 'Driving_License']

llm = ChatGroq(model="llama3-8b-8192")
tokenizer = LayoutLMTokenizer.from_pretrained(
    "microsoft/layoutlm-base-uncased")
model = LayoutLMForSequenceClassification.from_pretrained("./saved_model")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


def normalize_box(box, width, height):
    return [
        int(1000 * (box[0] / width)),
        int(1000 * (box[1] / height)),
        int(1000 * (box[2] / width)),
        int(1000 * (box[3] / height)),
    ]


def apply_ocr(example):
    image = convert_from_path(example['file_path'])[0]
    width, height = image.size

    ocr_df = pytesseract.image_to_data(image, output_type='data.frame')
    float_cols = ocr_df.select_dtypes('float').columns
    ocr_df = ocr_df.dropna().reset_index(drop=True)
    ocr_df[float_cols] = ocr_df[float_cols].round(0).astype(int)
    ocr_df = ocr_df.replace(
        r'^\s*$', np.nan, regex=True).dropna().reset_index(drop=True)

    words = [str(w) for w in ocr_df.text]
    coordinates = ocr_df[['left', 'top', 'width', 'height']]
    actual_boxes = [(x, y, x + w, y + h) for x, y, w, h in coordinates.values]
    boxes = [normalize_box(box, width, height) for box in actual_boxes]

    example['words'] = words
    example['bbox'] = boxes
    return example


def encode_example(example, max_seq_length=512, pad_token_box=[0, 0, 0, 0]):
    words = example['words']
    normalized_word_boxes = example['bbox']

    token_boxes = []
    for word, box in zip(words, normalized_word_boxes):
        word_tokens = tokenizer.tokenize(word)
        token_boxes.extend([box] * len(word_tokens))

    special_tokens_count = 2
    if len(token_boxes) > max_seq_length - special_tokens_count:
        token_boxes = token_boxes[: (max_seq_length - special_tokens_count)]

    token_boxes = [[0, 0, 0, 0]] + token_boxes + [[1000, 1000, 1000, 1000]]
    encoding = tokenizer(
        ' '.join(words), padding='max_length', truncation=True)
    input_ids = tokenizer(' '.join(words), truncation=True)["input_ids"]
    padding_length = max_seq_length - len(input_ids)
    token_boxes += [pad_token_box] * padding_length
    encoding['bbox'] = token_boxes
    return encoding


def predict_llms(text):
    from langchain_core.messages import HumanMessage, SystemMessage

    messages = [
        SystemMessage("The given text is extracted from a scanned PDF document using OCR. Based on the text, return what type of document label it is in maximum of 3 words only. Refrain from using any adjectives, be as straight forward and to the point as possible. For example: cards, credit cards, application form, etc. If nothing can be deduced directly, return Nan."),
        HumanMessage(text),
    ]
    return llm.invoke(messages).content


def predict(test_data):
    human_needed = False
    pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
    test_dataset = Dataset.from_pandas(test_data)
    updated_test_dataset = test_dataset.map(apply_ocr)

    df = pd.DataFrame.from_dict(updated_test_dataset)
    text = " ".join(df['words'][0])

    encoded_test_dataset = updated_test_dataset.map(
        lambda example: encode_example(example))

    encoded_test_dataset.set_format(type='torch', columns=[
                                    'input_ids', 'bbox', 'attention_mask', 'token_type_ids'])

    test_dataloader = torch.utils.data.DataLoader(
        encoded_test_dataset, batch_size=1, shuffle=False)

    for test_batch in test_dataloader:
        input_ids = test_batch["input_ids"].to(device)
        bbox = test_batch["bbox"].to(device)
        attention_mask = test_batch["attention_mask"].to(device)
        token_type_ids = test_batch["token_type_ids"].to(device)

        outputs = model(input_ids=input_ids, bbox=bbox, attention_mask=attention_mask,
                        token_type_ids=token_type_ids)

        classification_logits = outputs.logits
        print(f"Classification logits: {classification_logits}")
        classification_results = torch.softmax(
            classification_logits, dim=1).tolist()[0]
        print(f"Classification results: {classification_results}")

        if not classification_results:
            print("Error: Empty classification results")
            return text, "Error: Empty results", human_needed

        res = [int(round(classification_results[i] * 100))
               for i in range(len(classes))]

        if len(classification_results) != len(classes):
            print(f"Error: Mismatched lengths - Results: {
                  len(classification_results)}, Classes: {len(classes)}")
            return text, "Error: Mismatched results and classes", human_needed

        if any(value > 90 for value in res):
            prediction = (outputs.logits.argmax(-1).squeeze().tolist())
            return text, classes[prediction], human_needed
        else:
            prediction = predict_llms(text)
            human_needed = True
            return text, prediction, human_needed


st.title("Document Classifier")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    data = {'file_path': [file_path]}
    df = pd.DataFrame(data)

    text, prediction, human_needed = predict(df)

    st.subheader("Extracted Text:")
    st.text(text)

    st.subheader("Prediction:")
    st.text(prediction)
