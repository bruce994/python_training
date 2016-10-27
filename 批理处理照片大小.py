#import Image, os
import os
from PIL import Image  
   
def resize(fname):  
    img = Image.open(fname)  
         
    ratio = float(img.size[0]) / img.size[1]  
    width = int(ratio > 1 and 1024 or 1024 * ratio)  
    height = int(ratio > 1 and 1024 / ratio or 1024)  
      
    resized_img = img.resize((width, height), Image.ANTIALIAS)  
    basename, extension = os.path.splitext(fname)  
    resized_img.save(basename+'_resized.jpg')  
   
if __name__ == '__main__':  
    path = os.path.abspath(os.curdir)  
    dirList = os.listdir(path);  
    for fname in dirList:  
        basename, extension = os.path.splitext(fname)  
        if extension.lower() == '.jpg':  
            resize(fname)  