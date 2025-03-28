import pdfplumber

def extract_resume_text(file_path):
    """Extract text from a PDF resume."""
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()
