#!/usr/bin/env python
#-*- coding:utf-8-*-
import socket
import thread
import time,os,shutil,platform,datetime,sys
import MySQLdb
import sqlite3

conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='26wz',charset='utf8', init_command='SET NAMES UTF8')    
cursor = conn.cursor()

cursor.execute("select title,bookname,sortid,body,addtime,id from dede_story_content  where body <> '' order by id ")

conn_l = sqlite3.connect('E:/Users/wang/Downloads/Book.db')
if (conn_l):
  print ("Connection successful")
else:
  print ("Connection not successful")
  exit()

curs_l = conn_l.cursor()
for row in cursor.fetchall():
	title = row[0].encode('utf-8')
	bookname = row[1].encode('utf-8')
	sortid = row[2]
	body = row[3].encode('utf-8')
	body = body.replace("'","''")	
	addtime = row[4]
	
	#判断是否已经存在
	cc = conn_l.execute("select id from bc_booklist where bookname='"+bookname+"' and title='"+title+"' ")
	if cc.fetchone() is not None :
		print title + " is exist"
		continue
	
	sql = "insert into bc_booklist (bookname,title,body,sortid,addtime) values('"+bookname+"','"+title+"','"+body+"',"+str(sortid)+","+str(addtime)+");"
	print row[5]
	result = curs_l.execute(sql)
	conn_l.commit()
conn_l.close()
conn.close()


'''
cursor.execute("select id,bookname,author,description,pubdate from dede_story_books order by id")
conn_l = sqlite3.connect('E:/Users/wang/workspace/OnlieStory2/assets/Book.db')
if (conn_l):
  print ("Connection successful")
else:
  print ("Connection not successful")

curs_l = conn_l.cursor()

for row in cursor.fetchall():
	print row[1].encode('utf-8')
	bookname = row[1].encode('utf-8')
	writer = row[2].encode('utf-8')
	summary = row[3].encode('utf-8')
	addtime = row[4]
	
	#判断是否已经存在
	cc = conn_l.execute("select id from bc_bookname_copy where bookname='"+bookname+"' and writer='"+writer+"' ")
	if cc.fetchone() is not None :
		print bookname + " is exist"
		continue
	
	sql = "insert into bc_bookname_copy(bookname,writer,summary,addtime) values('"+bookname+"','"+writer+"','"+summary+"',"+str(addtime)+");"
	result = curs_l.execute(sql)
	conn_l.commit() #sqlite 还要提交
	print row[0]
conn_l.close()
conn.close()
'''


'''
dir = "E:\\Users\\wang\\Downloads\\public_html\\data\\textdata\\1"   #Windows
d = {'<?php error_reporting(0); exit();':'','?>':'',"'":"''"}

conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='26wz',charset='utf8', init_command='SET NAMES UTF8')    
cursor = conn.cursor()

for parent,dirnames, filenames in os.walk(dir):
	for filename in filenames:
		filename_path = os.path.join(parent, filename)
		content = file(filename_path,'r').read()
		for k,v in d.items():
			content = content.replace(k,v)
		reps = [r"<a[^>]+>",r"<\/a>"]
		for rep in reps:
			regex = re.compile(rep)
			content = regex.sub("", content)
		
		pattern = re.compile(r'[^\d]+(\d+)')
		match = pattern.match(filename)
		if match:
			id =  match.group(1)
			sql = "update dede_story_content set body='"+content.strip()+"' where id="+id
			cursor.execute(sql)
			conn.commit()
			print id
		
conn.close()			

'''
