import glob
import PyPDF2
from PyPDF2 import PdfFileMerger

# fetch all the files from the path provided
txtfiles = []
for file in glob.glob("*.pdf"):
    txtfiles.append(file)

# create object instance of PdfFileMerger
merger = PdfFileMerger()

# merge all the provided pdfs
for pdf in txtfiles:
    merger.append(open(pdf, 'rb'))

# save the newly merged pdf
with open('merged.pdf', 'wb') as fout:
    merger.write(fout)