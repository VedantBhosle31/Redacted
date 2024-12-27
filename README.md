# Redacted

# Model Setup and Execution Guide

This guide will walk you through setting up and running the model on a system with the necessary dependencies installed.

1. ## Prerequisites

Before running the model, you need to install the following system dependencies:

### Install Tesseract OCR and Poppler Utilities

Run the following commands to install the required dependencies:

```bash
sudo apt-get update
sudo apt-get install -y tesseract-ocr
sudo apt-get install -y libtesseract-dev
sudo apt-get install -y poppler-utils
```

#### macOS

```bash
brew install tesseract

brew install tesseract-lang

brew install poppler
```

### windows

1. Download the latest Tesseract Windows installer from:
   https://github.com/UB-Mannheim/tesseract/wiki

2. Follow the installation steps provided in the installer.

3. Add the Tesseract installation path to your system PATH.

4. Download and install Poppler for Windows from:
   http://blog.alivate.com.au/poppler-windows/

### Update tesseract's path on lines 33 and 111 in model/main.py

### Setting Up a Python Virtual Environment

Follow these steps to create and activate a Python virtual environment (venv) for the project.

1. Create venv

```bash
python -m venv venv
```

2. Activate venv

On macos / linux

```
source venv/bin/activate
```

On Windows

```
venv\Scripts\activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the model

```
cd model
```

```
streamlit run main.py
```
