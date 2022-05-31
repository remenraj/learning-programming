# Extract all texts from doc files

import os, docx


def get_text(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


os.chdir(os.path.dirname(__file__))


print(get_text("demo.docx"))