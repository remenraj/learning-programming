# Example program to combine PDF files

import PyPDF2, os


# change working directory
os.chdir(os.path.dirname(__file__))


pdf_file_1 = open(file="meetingminutes.pdf", mode="rb")
pdf_file_2 = open(file="meetingminutes2.pdf", mode="rb")

reader_1 = PyPDF2.PdfFileReader(pdf_file_1)
reader_2 = PyPDF2.PdfFileReader(pdf_file_2)

writer = PyPDF2.PdfFileWriter()

# add pages to writer
for page_num in range(reader_1.numPages):
    page = reader_1.getPage(pageNumber=page_num)

    writer.addPage(page=page)

for page_num in range(reader_2.numPages):
    page = reader_2.getPage(pageNumber=page_num)

    writer.addPage(page=page)
    
    
output_file = open("combined_minutes.pdf", mode="wb")
writer.write(output_file)
output_file.close()

pdf_file_1.close()
pdf_file_2.close()
