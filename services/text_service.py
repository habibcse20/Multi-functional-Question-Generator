from PyPDF2 import PdfReader

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def split_sentences(text):
    return [s.strip() for s in text.split('.') if len(s.split()) > 6]

