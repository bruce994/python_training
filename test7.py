#!/usr/bin/env python
#-*- coding:utf-8-*-
# 去掉文件中 <a... 链接
import socket
import thread
import time,os,shutil,platform,datetime,sys
import MySQLdb
import sqlite3
import re

'''
filename_path = "E:\\Users\\wang\\Downloads\\public_html\\data\\textdata\\1\\bk3813.inc"
content = file(filename_path,'r').read()
#content = content.decode(')
#print content
pattern = re.compile(r".*<a.*</a>.*",re.S) #re.S 匹配包括’/n’的所有字符
match = pattern.match(content)
if match:
	reps = [r"<a.*</a>"]
	for rep in reps:
		regex = re.compile(rep)
		content = regex.sub("", content)				
		print content
'''


dir = "E:\\Users\\wang\\Downloads\\public_html\\data\\textdata\\3"   #Windows
for parent,dirnames, filenames in os.walk(dir	):
	for filename in filenames:
		filename_path = os.path.join(parent, filename)
		content = file(filename_path,'r').read()

		pattern = re.compile(r".*<a.*</a>.*",re.S) #re.S 匹配包括’/n’的所有字符
		match = pattern.match(content)
		if match:
			reps = [r"<a.*</a>"]
			for rep in reps:
				regex = re.compile(rep)
				content = regex.sub("", content)				
				file_write = open(filename_path, 'w')
				file_write.write(content)
				file_write.close				
				print filename_path

		
		


			
			
