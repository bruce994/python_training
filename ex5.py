#-*- coding: UTF-8 -*-
import sys
import string
import time
print sys.version
import re
import os,shutil,platform,datetime
import urllib2


response = urllib2.urlopen("http://market.ctei.gov.cn/")
headers = response.info()
data = response.read()


pattern = re.compile(r'[\s\S]*<td width="310" valign="top">([\s\S]*)<table width="100%" height="98" border="0" cellpadding="0" cellspacing="0">[\s\S]*')
match = pattern.match(data)
if match:
    # 使用Match获得分组信息
    print match.group(1)

