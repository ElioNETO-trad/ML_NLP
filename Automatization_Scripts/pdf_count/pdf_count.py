import pdfplumber

word_count = 0
with pdfplumber.open("213-04-ARQ-0") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            word_count += len(text.split())

print(f"Total words: {word_count}")