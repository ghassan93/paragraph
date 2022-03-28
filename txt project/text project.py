
txt = open("inputText.txt","r")
read_txt = txt.read()
txt_split=read_txt.split('\n')
while '' in txt_split:
    txt_split.remove('')
while ' ' in txt_split:
    txt_split.remove(' ')
        
keywords=['Due date','deadline','QA date','Mandatory','Meeting','walkthrough','Intent to bid','Manual','References','Surety','bond','Maintenance','support','Timeframe','timeline','Signature','Submittal format','hard copy(ies)','Font','Page limit']
multi_keywords = ['Original','copy','copies']
print(txt_split)  
# for x in txt_split:
#     for i in keywords:
#         if i in x : 
#             pass
            # (i)
            #return x
          
# c='Original'            
# for y in txt_split:
#     for i in multi_keywords:
        
#        if  i in y:
#          print (y)         
           
# txt.close()
    

    # with open("output.txt","+a")as outfile:  
    #     outfile.write("\n".join(x))
  
    #print(txt_split)  
  



