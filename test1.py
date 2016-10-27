#-*- coding: UTF-8 -*-
import sys
import string
import time
print sys.version
import re
import MySQLdb


conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='health720_mail',charset='utf8', init_command='SET NAMES UTF8')    
cursor = conn.cursor()

'''
line = 34343434
line = str(line) + '@qq.com'
print line
sys.exit()
'''


#读取文件
myfile = open("wuhan.txt")
for line in myfile.readlines():
    line = line[0:-1] + "@qq.com" #去掉换行
    #判断是否已经存在
    cursor.execute("select id from qq_email where email='"+line+"'")
    if cursor.fetchone() is not None :
        print line + " is exist"
        continue       
    #插入
    cursor.execute("INSERT INTO qq_email(email, area) VALUES('"+line+"', '武汉')")
    conn.commit()
    print line + " success"
myfile.close()
conn.close()


#print datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
#print cursor.fetchall()[0]













