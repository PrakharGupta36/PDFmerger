import PyPDF2
import os

from PyPDF2.merger import PdfFileMerger

pdfs = [pdf for pdf in os.listdir() if pdf.endswith('.pdf')]
if len(pdfs) == 0:
        print("No pdfs found")
else:
    output = PdfFileMerger()
    for i in pdfs:
        output.append(i)
        
    with open("output.pdf","wb") as f:
        output.write(f)
