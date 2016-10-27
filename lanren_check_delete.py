#! /usr/bin/env python
#-*- coding: UTF-8 -*-
import sys
import os
import string
import time
print sys.version
import re
import shutil

path = "/Users/apple/Downloads/aaaa/"
dirList = os.listdir(path)

check = ['06f59cc2e3573af9033df8a7bfa2b6d0.txt', 'Opera_16.0.1196.80_Setup.zip','404.html','pc-wap.xml','53c440f20c9ad8f16453a3c8026914a1.html','plus','addweixin.html','QQqunlianmeng','ad.html','robots.txt','banquanshengming','rss.xml','bdunion.txt','shenghuofuwu','changjianwenti','shoujijstexiao','data','shoujiwangzhanyuanma','diannaowangluo','special','diywap','tags.php','f6a44490d2fc473.html','templets','favicon.ico','ThinkPHP','favicon.png','tool','fengbaobao','ueditor','goto.php','uploads','guanggaofuwu','User','guanyuwomen','wap','HTML5','wap.php','images','wcs','include','wdzposth.php','index1.php','weiceshi','index.html','weiguanwang','jiaoyuxuexi','weixinapi','JS','weixindingyuehao','lanren_admin','weixingongzhongpingtai','lanrengongjuxiang','weixin.php','lanrenmb.php','weixinsucai','lanren.png','womendejiazhiguan','lianxiwomen','yidongyunying','lightApp','yonghutougao','meirifuli','yulexiuxian','misc','zt','lanren_check_delete.py']

#print len(check)

for fname in dirList:
	if fname not in check:
		tmp = os.path.join(path, fname)
		if os.path.isdir(tmp)==False:
			os.remove(tmp)
		if os.path.isdir(tmp)==True:
			shutil.rmtree(tmp)
		print tmp












