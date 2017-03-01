#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import sys
import string
import time
print sys.version
import re
import os,shutil,platform,datetime
import calendar
starttime = datetime.datetime.now()


year = starttime.strftime("%Y")
month = starttime.strftime("%B")[:3]
day = starttime.strftime("%d")
hour = starttime.strftime("%H")
current_date =  day + "/" + month + "/" + year + ":" + hour
#current_date =  day + "/" + month + "/" + year

blacklist_date = "/home/Tool/blacklist_date.txt"
if os.path.isfile(blacklist_date):
    f = open(blacklist_date, 'r')
    date1 = f.read()
    if date1 != current_date :
        os.system("ipset flush blacklist")  #清空blacklist 集合
        f = open(blacklist_date, 'w')
        f.write(current_date)
        f.close()
else:
    f = open(blacklist_date, 'w')
    f.write(current_date)
    f.close()

ipNum = "800"
log = ['/home/log/ttp.wf0933.cn-','/home/log/vote.lanrenmb.com-']

for f in log:
    ssh_1 = "cat "+f+starttime.strftime("%Y-%m-%d")+".access.log |grep '"+current_date+"' |cut -d ' ' -f 1 |sort |uniq -c | awk '{if ($1 > "+ipNum+") print $2}'|sort -nr |less | awk '{print \"ipset add blacklist\",$0}'|sh"
    #print ssh_1
    os.system(ssh_1)


endtime = datetime.datetime.now()
print str((endtime - starttime).seconds) + ' sencond' #执行时间 
