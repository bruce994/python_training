#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#电话导出文件去掉空电话
import sys
import string
import time
import re



filename = "/Users/apple/Downloads/11111.csv" 

content = ""
i=0
with open(filename) as f:
	for line in f:
		i=i+1
		ar = line.split(',')
		if not ar[18]=="\"\"":
			content = content + line
			print i
	file_write = open("tel.csv", 'w')
	file_write.write(content)
	file_write.close

