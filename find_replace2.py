#-*- coding: UTF-8 -*-
import sys
import string
import time
print sys.version
import re
import os,shutil,platform,datetime
import urllib
import os,binascii,random
import imghdr


starttime = datetime.datetime.now()


content = file('index_bianjiqi.htm','r').read()
i=0
m = re.findall(r'<img.*src="https:\/\/mmbiz\.qlogo\.cn[^"]*".*>',content)
for item in m:
	m1 = re.findall(r'https:\/\/mmbiz\.qlogo\.cn[^"]*',item)
	if(m1):
		i = i+1
		# if i<498:
		# 	continue
		try:
			n_file = str(i)
			urllib.urlretrieve(m1[0], n_file)
			ext = imghdr.what(n_file)
			if ext is None:
				continue
			os.rename(n_file, n_file+"."+ext)

			n_a = 'http://www.lanrenmb.com/images/guanzhu2/'+n_file+"."+ext
			replace_str = 'class="lanrenmb_com" data-wxsrc="'+m1[0]+'"  src="'+n_a+'"'
			n_item = item.replace('src="'+m1[0]+'"',replace_str)

			content = content.replace(item,n_item)

		except Exception, e:
			raise
		else:
			pass
		finally:
			pass

		print i


with open('bb.html','w') as f:
    f.write(content)


endtime = datetime.datetime.now()
print str((endtime - starttime).seconds) + ' sencond' #执行时间

