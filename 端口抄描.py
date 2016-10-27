#!/usr/bin/env python
#-*- coding:utf-8-*-
import socket

ip='58.221.81.62'
startport=22
endport=100000
success_port = ""
for port in range(startport,endport+1):
	print('Port scaning:%d' % port)
	try:
		sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sk.settimeout(1)
		sk.connect((ip,port))
		print('Server %s port %d OK!' % (ip,port))
		success_port += str(port) + '\n'				
	except Exception:
		print('Server %s port %d is not connected!' % (ip,port))
sk.close()

if success_port != "" :
	file_write = open("success_port.txt", 'w')
	file_write.write(success_port)
	file_write.close
