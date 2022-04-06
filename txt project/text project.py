import os
import pdfplumber


# convert pdf to output file as processing.text
processing = open("processing.txt","w")
with pdfplumber.open('hh-ocr-combined.pdf') as pdf:
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
if os.path.exists("processing.txt"):
  os.remove("processing.txt")
else:
  print("The file does not exist")
  
