#-*- coding: UTF-8 -*-
#批量改名
import sys
import os
import string
import time
print sys.version
import re

path = "E:\\Users\\wang\\Downloads\\2012\\"
dirList = os.listdir(path)

i=0
for fname in dirList:
	i+=1
	print os.path.join(path, "2012_"+ str(i) + ".jpg")
	os.rename(os.path.join(path, fname), os.path.join(path, str(i) + ".jpg"))




#print datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
#print cursor.fetchall()[0]













