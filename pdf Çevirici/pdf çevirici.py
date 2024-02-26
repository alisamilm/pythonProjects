from pdf2docx import Converter

pdf_file = "pdf.pdf"
docx_file = "pdf.docx"

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()