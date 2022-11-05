import pytesseract
from PIL import Image
import datetime
import cv2
import sys
import os
import os.path
import re
import numpy as np

pytesseract.pytesseract.tesseract_cmd= r'C:\Users\admin\AppData\Local\Tesseract-OCR\tesseract'
img=Image.open('two.jpg')
text=pytesseract.image_to_string(img)
#print(text,end='')
#print(type(text))
ans=text.split("\n")
print(ans)
for i in ans:
    if i==str(''):
        ans.remove(i)
print(ans)    
#ans.remove('')

s=' '
a=s.join(ans)
print(a)


d={'Name':None,'DOB':None,'Gender':None,'Mobile_No':None,'Aadhar_No':None}
import regex as re
pattern1= '\d\d\/\d\d\/\d\d\d\d'
pattern2='\d{4}\s?\d{6}'
pattern3= 'MALE|FEMALE'
pattern4= '\s\d{4}\s\d{4}\s\d{4}'

l1=re.findall(pattern1,a)
l2=re.findall(pattern2,a)
l3=re.findall(pattern3,a)
l4=re.findall(pattern4,a)

print(l1,l2,l3)

d['Name']=ans[1]
d['DOB']= l1[0]
d['Gender']= l3[0]
d['Mobile_No']= l2[0]
d['Aadhar_No']=l4[0]
print(d)

