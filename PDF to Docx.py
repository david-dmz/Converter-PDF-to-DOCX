from fileinput import close

from pdf2docx import Converter

pdf = "input.pdf"
docx = "output.docx"

print("Converting...")

cv = Converter(pdf)
cv.convert(docx, start =0, end=None)
cv.close()

print("Done! File saved as", docx)