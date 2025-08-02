import fitz
import PyPDF2
import pdfplumber

# from PyPDF2 import PdfReader

# reader = PdfReader("Arav_Mehta_Resume.pdf")

# print(f"The PDF has {len(reader.pages)} pages.")

# page = reader.pages[0]

# print(page.extract_text())


# #using pdf plumber

# import pdfplumber

# with pdfplumber.open("Arav_Mehta_Resume.pdf") as pdf:
#    page = pdf.pages[0]
#    print(page)


# # Extract tables from the first page
# with pdfplumber.open("sample_title_report.pdf") as pdf:
#   # try putting the page number where there is a table
#     page = pdf.pages[12]
#     tables = page.extract_tables()
#     for table in tables:
#         for row in table:
#             print(row)


import fitz  # PyMuPDF

# Load the PDF
doc = fitz.open("Arav_Mehta_Resume.pdf")

page = doc[0]
# print(page.get_text())

# print("PDF Metadata:", doc.metadata)


pix = page.get_pixmap()
pix.save("page1.jpg")