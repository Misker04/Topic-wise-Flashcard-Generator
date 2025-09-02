import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    text = ""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8")
