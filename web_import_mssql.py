#-*- coding: utf-8 -*-
import sys
import string
import time
print sys.version
import re
import os,shutil,platform,datetime
import urllib2,cgi
import pymssql
import cgitb; cgitb.enable() # Optional; for debugging only
print "Content-Type: text/html;charset=utf-8"
print ""


arguments = cgi.FieldStorage()
#for i in arguments.keys():
#	print arguments[i].value


Abig = arguments['Abig'].value
Asamll = arguments['Asamll'].value
Title = arguments['Title'].value
Content = arguments['Content'].value
Admin = arguments['Laccount'].value
Auth = arguments['Auth'].value
if "Key" not in arguments:
	Key = ""
else:
	Key = arguments['Key'].value
if "Summary" not in arguments:
	Summary = ""
else:
	Summary = arguments['Summary'].value

if(Auth != "Lq7JRzPBpR"):
	print "识别码不正确".decode("gb2312").encode("utf-8")
	exit()

Title_ = Title.decode("utf-8").encode("gb2312").replace("'","''")
Content_ = Content.decode("utf-8").encode("gb2312").replace("'","''")
Key_ = Key.decode("utf-8").encode("gb2312").replace("'","''")
Summary_ = Summary.decode("utf-8").encode("gb2312").replace("'","''")
Abig_ = Abig.decode("utf-8").encode("gb2312")
Asamll_ = Asamll.decode("utf-8").encode("gb2312")
Admin_ = Admin.decode("utf-8").encode("gb2312")

Uid = 420 #后台会员ID

conn = pymssql.connect(host='58.221.208.219:1433', user='test_ntjj_com', password='142536', database='test_ntjj_com')
cur = conn.cursor()

cur.execute("SELECT ID FROM t_Member_Member WHERE Laccount=%s",Admin_)
row = cur.fetchone()
if row is None :
	print Admin + ' 用户不存在'.decode("gb2312").encode("utf-8")
	exit()
else:
	Uid = row[0]

cur.execute("SELECT ID,Pid,Aname FROM t_S_Articlebigtype WHERE Aname=%s",Abig_)
row = cur.fetchone()
if row is None :
	print Abig + ' (大类)不存在'.decode("gb2312").encode("utf-8")
else:
	ID,Pid,Aname = row	
	cur.execute("SELECT ID,Pid FROM t_S_Articlebigtype WHERE Aname=%s and Pid=%d",(Asamll_,ID))
	row = cur.fetchone()
	if row is None :
		print Asamll + ' (小类)不存在'.decode("gb2312").encode("utf-8")
	else:
		Asamllid,Abigid = row
		sql = "insert into t_S_Article(Title,Abigid,Asamllid,keys,Author,Source,Isblank,Ishome,Istop,Faceimg,Ishot,Summary,Content,Videotype,Vsource,Isrecommend,Hits,Dorder,Iscomment,State,LiveWordCount,Uid) values('"+Title_+"',"+str(Abigid)+","+str(Asamllid)+",'"+Key_+"','未知','网络转载','',2,2,'',2,'"+Summary_+"','"+Content_+"',0,'',0,0,0,1,2,0,"+str(Uid)+");"
		result = cur.execute(sql)
		conn.commit()
		print "成功".decode("gb2312").encode("utf-8")

conn.close()		


##http://www.ntjj.net/wang_import.py?Title=fdfdfdf&Abig=%E8%A1%8C%E4%B8%9A%E6%8A%A5%E9%81%93&Asamll=%E5%BB%BA%E6%9D%90%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF&Content=aaaaaaaaaaaaaaaaaaaa&Laccount=admin