# The PyPDF2 module can read and write PDFs.
# Opening a PDF is done by calling open() and passing the file object to PPdfFileReader().
# A Page object can be obtained from the PDF object with the getPage() method.
# The text from a Page object is obtained with the extractText() method, which can be imperfect.
# New PDFs can be made from PdfFileWriter().
# New pages can be appended to a writer object with the addPage() method.
# Call the write() method to save its changes.

# install PyPDF2 module: pip install PyPDF2

import PyPDF2, os



# change directory to cwd
os.chdir(os.path.dirname(__file__))

# open pdf file
pdf_file = open("meetingminutes.pdf", mode="rb")   # rb = read binary

reader = PyPDF2.PdfFileReader(pdf_file)

# print number of pages
print(reader.numPages)

page = reader.getPage(pageNumber=0)
print(page.extract_text())

# print all pages
for page_num in range(reader.numPages):
    print(reader.getPage(pageNumber=page_num).extract_text())
    
pdf_file.close()