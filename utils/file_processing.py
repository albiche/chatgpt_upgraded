import PyPDF2
import docx2txt
import pandas as pd

def extract_text_from_file(file):
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = docx2txt.process(file)
    elif file.type == "text/plain":
        text = file.read().decode("utf-8")
    elif file.type == "text/csv":
        df = pd.read_csv(file)
        text = df.to_string()
    else:
        text = "Type de fichier non pris en charge."
    return text

def extract_text_from_files(files):
    context = ""
    for file in files:
        context += extract_text_from_file(file) + "\n\n"
    return context
