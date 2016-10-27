#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import sys
import string
import time
import re

filename = "/vhs/kangle/ext/tpl_php52/php-templete.ini" #查找所在目录路径  Linux
find_str1 = "fsockopen,pfsockopen,"

content = file(filename,'r').read()
if content.find(find_str1) > -1 :
        print 0
else:
        content = content.replace("disable_functions = ","disable_functions = "+find_str1)
        file_write = open(filename, 'w')
        file_write.write(content)
        file_write.close

from subprocess import call
call(["service","kangle","restart"])  #重启服务