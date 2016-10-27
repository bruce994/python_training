#!/usr/bin/env python
#-*- coding:utf-8-*-
import socket
import thread
import time,os,shutil,platform,datetime,sys,re
import MySQLdb
import sqlite3



conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='test',charset='utf8', init_command='SET NAMES UTF8')    
cursor = conn.cursor()

cursor.execute("select title,body,id from jzwj_archives as a join jzwj_addonarticle as b  on a.id=b.aid  where title <> '' and id<8542 order by id desc   ")

for row in cursor.fetchall():
    title = row[0]
    content = row[1].encode('utf-8')
    id =  row[2]


    title = title.replace("?","")
    title = title.replace(",","")
    title = title.replace("!","")
    title = title.replace(".","")
    title = title.replace("\"","")
    title = title.replace("|","")
    title = title.replace("/","")
    
    
    tmp2=''
    for x in title:
        tmp2 += x + ' '

    tmp2 = tmp2[:-1] + '.txt'

    try:
        file_write = open(tmp2, 'wb')
    except Exception, e:
        continue
    else:
        reps = [r"<[^>]+>",r"&nbsp;"]
        for rep in reps:
            regex = re.compile(rep)
            content = regex.sub("", content)
        
        file_write.write(content)
        file_write.close
        print str(id) + ":" +tmp2

    
 
conn.close()







