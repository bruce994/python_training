#-*- coding: UTF-8 -*-
import sys
import string
import time
print sys.version  # 打印版本
print sys.modules  # 打印模板
import re



#读取文件
myfile = open("wuhan.txt")
file_object = open('wuhan1.txt', 'w')
for line in myfile.readlines():
    line = line[0:-1] + "@qq.com" #去掉换行
    #判断是否已经存在
    file_object.writelines(line + '\r\n')
    print line
myfile.close()
file_object.close()



#print datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
#print cursor.fetchall()[0]













