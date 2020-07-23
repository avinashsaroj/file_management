import os, glob
from PIL import Image
import shutil,fleep
path='D:/Downloads'
dest='D:/text_files'
dest1='D:/image_files'
dest2='D:/pdf_files'
dest3='D:/mp3_files'
dest4='D:/softwares'
dest5='D:/zip_files'

os.chdir(path)
files=os.listdir(path)
for f in files:
    if f.endswith('.txt'):
        shutil.move(f,dest)
    if (f.endswith('.png')) or (f.endswith('.jpg')):
        shutil.move(f,dest1)
    if f.endswith('.pdf'):
        shutil.move(f,dest2)
    if f.endswith('.mp3'):
        shutil.move(f,dest3)
    if f.endswith('.exe'):
        shutil.move(f,dest4)
    if f.endswith('.zip'):
        shutil.move(f,dest5)


