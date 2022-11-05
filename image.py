poppler_path= 'C:/Users/admin/Desktop/Aadhar/poppler-22.04.0/Library/bin'
import os
from pdf2image import convert_from_path

pdf_path=r'C:\Users\admin\Desktop\Aadhar\Aadhar.pdf'
saving_folder=r'C:\Users\admin\Desktop\Aadhar'

def pdf2images(pdf_path):
    pages = convert_from_path(pdf_path=pdf_path,poppler_path=poppler_path)
    count = 0
    for page in pages:
        count +=1
        img_name=f'img-{count}.jpeg'
        page.save(os.path.join(saving_folder,img_name), 'JPEG')


pdf2images(pdf_path)
