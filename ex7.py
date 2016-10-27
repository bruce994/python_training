#!/usr/bin/env python
#-*- coding:utf-8-*-
import socket
import thread
import time,os,shutil,platform,datetime,sys
import MySQLdb
import sqlite3
import re

conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='xinyue_fk',charset='utf8', init_command='SET NAMES UTF8') 
cursor = conn.cursor()
curs = cursor.execute("select aid,body from dede_addonarticle")
for row in cursor.fetchall():
	aid = row[0]
	body = row[1]
	body = body.replace("'","''")	


	tmp = u'温馨提示[\s\S]*' #包括换行符
	reps = [r"<a[^>]+>",r"<\/a>",tmp,r"<img[^>]+>"]
	for rep in reps:
		regex = re.compile(rep)
		body = regex.sub("", body)

	
	sql = "update dede_addonarticle set body='"+body+"' where aid="+str(aid)
	result = cursor.execute(sql)
	conn.commit()

	print aid

# conn_l.close()
conn.close()	


