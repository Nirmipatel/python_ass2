# 20CE095 Nirmipatel
#Practical 10: Generate PDF file of your 3rd Semester Mark-sheet
#
import img2pdf
from PIL import Image
import os


img_path = "D:\sem3_result.png"
pdf_path = "D:\esult.pdf"
image = Image.open(img_path)
pdf_bytes = img2pdf.convert(image.filename)

file = open(pdf_path,"wb")
file.write(pdf_bytes)
image.close()
file.close()
print("Successfully made pdf file")