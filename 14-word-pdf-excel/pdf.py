import PyPDF2, os

# PDF files fairly complex some files might not work
print(os.getcwd())

# open in read binairy (rb) mode
pdfFile = open('meetingminutes1.pdf', 'rb')

# open with PyPDF filereader
reader = PyPDF2.PdfFileReader(pdfFile)

# get number of pages
print(reader.numPages)

# get Page object 0 indexed
page = reader.getPage(0)

# extract text from page object
print(page.extractText())

# loop to get all page objects and extract them
for pageNum in range(reader.numPages):
  print(reader.getPage(pageNum).extractText())

# combine two pdf files into one
pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes1.pdf', 'rb')
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

# create new writer object
writer = PyPDF2.PdfFileWriter()

# loop over all pages and write to new writer object
for pageNum in range(reader1.numPages):
  page = reader1.getPage(pageNum)
  writer.addPage(page)

# same for second file
for pageNum in range(reader2.numPages):
  page = reader2.getPage(pageNum)
  writer.addPage(page)
  
# open future combined pdf files in write binairy
outputFile = open('combinedminutes.pdf', 'wb')

# write writer object to outputFile
writer.write(outputFile)

# close
outputFile.close()
pdf1File.close()
pdf2File.close()