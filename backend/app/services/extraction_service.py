from pathlib import Path
import pdfplumber
from docx import Document
def extract_text(file_path):
    file_type=Path(file_path).suffix.lower()
    if file_type=='.pdf':
        return extract_pdf(file_path)
    elif file_type=='.docx':
        return extract_docx(file_path)
    else:
        raise ValueError("Unsupported file type")

def extract_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text=""
        for page in pdf.pages:
            page_text=page.extract_text()
            if page_text:
                text+=page_text+"\n"
        return text.strip()
    
def extract_docx(file_path):
    document=Document(file_path)
    text=""
    for paragraph in document.paragraphs:
        para_text=paragraph.text
        if para_text:
            text+=para_text+"\n"
    return text.strip()