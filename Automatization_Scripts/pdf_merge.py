import os
from pypdf import  PdfReader, PdfWriter

# Set input directory path

input_directory = input("Choose your path folder:" )

print(input_directory)

pdfs = [f for f in os.listdir(input_directory) if f.endswith('.pdf')]

print(pdfs)

if not pdfs:
    print('No PDF files found in the directory.')
    exit()

output_path = os.path.join(input_directory, "merged.pdf")

try:

#Initialize writer
    writer = PdfWriter()

    # reach each PDF and add to writer

    for file in pdfs:
        reader = PdfReader(os.path.join(input_directory, file))
        for page in reader.pages:
            writer.add_page(page)


    with open(output_path, "wb") as f:
        writer.write(f)

except Exception as e:
    print(f"Error merging PDFs: {str(e)}")

print(f"Merged successfully! File save at: {output_path}")


