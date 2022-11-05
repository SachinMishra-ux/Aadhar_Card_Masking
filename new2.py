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
img=Image.open('tikka.jpg')
text=pytesseract.image_to_string(img)
print(text,end='')
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
start=a.rfind("Address")

a1=a[start+9:]


d={'Address':None}
import regex as re
pattern1= '.+\d{6}'

l1=re.findall(pattern1,a1)
print(l1)

d['Address']=l1[0]

print(d)