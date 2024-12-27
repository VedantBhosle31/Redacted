const Validate = () => {
    return (
        <div style={{ display: 'flex', height: '100vh' }}>
            <div style={{ flex: 1, borderRight: '1px solid #ddd', overflow: 'auto' }}>
                <object
                    data="/assets/aad.pdf"
                    type="application/pdf"
                    width="100%"
                    height="100%"
                >
                    <p>Alternative text - include a link <a href="/assets/aad.pdf">to the PDF!</a></p>
                </object>
            </div>

            <div style={{ flex: 1, padding: '20px' }}>
                <h2>Validate</h2>
                <p>Unique Identification Authority of India</p>
                <p>Enrolment No.: 2006/31627/36628</p>
                <p>To</p>
                <p>Vedant Sandeep Bhosle</p>
                <p>Plot No. 4</p>
                <p>Gurudatta Society, Narendra Nagar</p>
                <p>VTC: Nagpur</p>
                <p>District: Nagpur</p>
                <p>State: Maharashtra</p>
                <p>PIN Code: 440015</p>
                <p>Mobile: 9823043105</p>

            </div>
        </div>
    );
};

// Default export
export default Validate;
