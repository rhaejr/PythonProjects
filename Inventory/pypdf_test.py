import PyPDF2

pdffileobj = open('apache tm/damper.pdf')

pdfReader = PyPDF2.PdfFileReader(pdffileobj)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())