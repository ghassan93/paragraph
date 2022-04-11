import os			    # for magick and tesseract commands
import time			  # for epoch time
import calendar 	# for epoch time
from PyPDF2 import PdfFileMerger,PdfFileReader
import pdfplumber 


dir_files = [f for f in os.listdir(".") if os.path.isfile(os.path.join(".", f))]
epoch_time = int(calendar.timegm(time.gmtime()))
print(dir_files)

for file in dir_files: # look at every file in the current directory
	if file.endswith('.pdf'): # if it is a PDF, use it
		print('Working on converting: ' + file)
		# setup
		file = file.replace('.pdf', '') # get just the filepath without the extension
		folder = str(int(epoch_time)) + '_' + file # generate a folder name for temporary images
		combined = folder + '/' + file # come up with temporary export path
		# create folder
		if not os.path.exists(folder): # make the temporary folder
			os.makedirs(folder)
		# convert PDF to PNG(s)
		magick = 'convert -density 150 "' + file + '.pdf" "' + combined + '-%04d.png"'
		print(magick)
		os.system(magick)
		# convert PNG(s) to PDF(s) with OCR data
		pngs = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
		for pic in pngs:
			if pic.endswith('.png'):
				combined_pic = folder + '/' + pic
				print(combined_pic)
				tesseract = 'tesseract "' + combined_pic + '" "' + combined_pic + '-ocr" PDF'
				print(tesseract)
				os.system(tesseract)
		# combine OCR'd PDFs into one
		ocr_pdfs = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

		merger = PdfFileMerger()
		for pdf in ocr_pdfs:
			if pdf.endswith('.pdf'):
				merger.append(folder + '/' + pdf)

				

		merger.write(file + '-ocr-combined.pdf')
		merger.close()






dir_files = [f for f in os.listdir(".") if os.path.isfile(os.path.join(".", f))]
for file in dir_files:
	if file.endswith('-combined.pdf'):
		processing = open("processing.txt","w")
		with pdfplumber.open(file) as pdf:
			for page in pdf.pages:
				numpage=page.page_number
				txt=page.extract_text()
				processing.write(txt)
				print(txt)
		processing.close()  
				
		# cut text into paragraph
		txt = open("processing.txt","r")
		read_txt = txt.read()
		txt_split=read_txt.split('\n ')
		txt.close()
		while '' in txt_split:
			txt_split.remove('')
		while ' ' in txt_split:
			txt_split.remove(' ')
		print(txt_split)    
				
		multi_keywords = ['Original','copy','copies']

		output = open("outputText.txt","w")

		# search keywords in paragraph and write result in output file
		for paragraph in  txt_split:
			checker = []
			for word in multi_keywords:
				checker.append(bool(paragraph.count(word)))
			if sum(checker) > 1 :
				output.write(paragraph+'\n')
				
		output.close()

# remove processing.text
import os
import shutil
if os.path.exists("processing.txt"):
  os.remove("processing.txt")
else:
  print("The file does not exist")
  

#remove image folder converting
shutil.rmtree(folder)  
		
