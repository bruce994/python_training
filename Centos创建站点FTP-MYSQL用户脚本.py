#-*- coding:utf-8-*-
import sys
import string
import time
import re
import commands
import random
import MySQLdb

#user 表示创建的用户
#web 表示网站目录
#is_R 表示是否增加301跳转，默认不跳转
#is_db 表示是否创建mysql数据库
def main(user, web, is_R=0,is_db=0):
    chroot_list = "/etc/vsftpd/chroot_list"
    httpd_conf = "/etc/httpd/conf/httpd.conf"
    udir = "/home/www/"
    ulog = "/home/log/"
    db_host = '127.0.0.1'
    db_user = 'root'
    db_pass = 'qq@1149015928'
    httpd = """
# {web}
<VirtualHost *:80>
    DocumentRoot {udir}{web}
    ServerName {web}
    CustomLog "|/usr/sbin/rotatelogs {ulog}{web}-%Y-%m-%d.access.log 86400 480" common
    #ErrorLog "|/usr/sbin/rotatelogs  {ulog}{web}-%Y-%m-%d.error.log 86400 480"

	<IfModule itk.c>
	 AssignUserId {user} {user}
	</IfModule>

     <IfModule mod_bw.c>
          BandwidthModule On
          ForceBandWidthModule On
          Bandwidth all 1024000
          MinBandwidth all 50000
          LargeFileLimit * 500 50000
          MaxConnection all 6
     </IfModule>

    <IfModule mod_suphp.c>
        suPHP_UserGroup {user} {user}
    </IfModule>

<IfModule concurrent_php.c>
        php4_admin_value open_basedir "{udir}{web}:/usr/lib/php:/usr/php4/lib/php:/usr/local/lib/php:/usr/local/php4/lib/php:/tmp"
        php5_admin_value open_basedir "{udir}{web}:/usr/lib/php:/usr/local/lib/php:/tmp"
    </IfModule>
    <IfModule !concurrent_php.c>
        <IfModule mod_php4.c>
            php_admin_value open_basedir "{udir}{web}:/usr/lib/php:/usr/php4/lib/php:/usr/local/lib/php:/usr/local/php4/lib/php:/tmp"
        </IfModule>
        <IfModule mod_php5.c>
            php_admin_value open_basedir "{udir}{web}:/usr/lib/php:/usr/local/lib/php:/tmp"
        </IfModule>
        <IfModule sapi_apache2.c>
            php_admin_value open_basedir "{udir}{web}:/usr/lib/php:/usr/php4/lib/php:/usr/local/lib/php:/usr/local/php4/lib/php:/tmp"
        </IfModule>
    </IfModule>

</VirtualHost>
<Directory "{udir}{web}">
Options FollowSymLinks IncludesNOEXEC -Indexes
AllowOverride All
Order Deny,Allow
Allow from all
</Directory>
"""
    httpd_301 = """
# {web_301} 301
<VirtualHost *:80>
    ServerAdmin bruce147@hotmail.com
    ServerName {web_301}
    RewriteEngine On
    RewriteRule ^/(.*) http://{web}/$1 [L,R=301]
</VirtualHost>
"""


    # create user
    status, output = commands.getstatusoutput('useradd -d ' + udir + web + ' ' + user)
    print output

    password = render()

    #update password
    status, output = commands.getstatusoutput('echo "'+password+'"|passwd '+user+' --stdin')
    print output

    #nologin
    status, output = commands.getstatusoutput('usermod -s /sbin/nologin '+user)
    print output


    status, output = commands.getstatusoutput('chmod -R 777 '+ udir + web)
    print output

    # add ftp user
    insert(chroot_list, user)

    # service vsftpd restart
    status, output = commands.getstatusoutput('service vsftpd restart')
    print output

    # add httpd.conf
    httpd = httpd.replace("{web}", web)
    httpd = httpd.replace("{user}", user)
    httpd = httpd.replace("{udir}", udir)
    httpd = httpd.replace("{ulog}", ulog)
    if int(is_R) == 1:
        httpd_301 = httpd_301.replace("{web_301}", web.replace("www.", ""))
        httpd_301 = httpd_301.replace("{web}", web)
        httpd = httpd + httpd_301
    insert(httpd_conf, httpd)

    # service httpd restart
    status, output = commands.getstatusoutput('service httpd restart')
    print output

    print 'FTP用户名：'+user
    print 'FTP密码：'+password


    if int(is_db) == 1:
        dbname = 'db_'+user
        dbuser = user
        dbpass = password
        try:
            conn = MySQLdb.connect(host=db_host,user=db_user,passwd=db_pass)
            cursor = conn.cursor()
            cursor.execute('CREATE DATABASE '+dbname+' CHARACTER SET utf8 COLLATE utf8_general_ci;')

            cursor.execute("CREATE USER '"+dbuser+"'@'localhost' IDENTIFIED BY '"+dbpass+"';GRANT USAGE ON *.* TO '"+dbuser+"'@'localhost' IDENTIFIED BY '"+dbpass+"' WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;GRANT ALL PRIVILEGES ON  `"+dbname+"` . * TO  '"+dbuser+"'@'localhost' WITH GRANT OPTION ;")
            print '数据库：'+dbname
            print '数据库用户名：'+dbuser
            print '数据库密码：'+dbpass
        except:
            print 'msyql Connection not successful'


def insert(str_file, str_cnt):
    output = []
    f = open(str_file)
    for i in f.readlines():
        output.append(i)
    f.close()
    output.append(str_cnt + "\n")
    f = open(str_file, "w+")
    for i in output:
        f.writelines(i)
    f.close

def render(len=8, num_flag=True, low_flag=True, up_flag=True, special_flag=True):
    num = "0123456789"
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special = "~!@#$%^&*()[]{}_=+-"

    str = ''
    if num_flag:
	    str += num
    if low_flag:
	    str += lower
    if up_flag:
	    str += upper
    if special_flag:
	    str += special
    if str == '':
	    str = num + lower
    return string.join(random.sample(str, len)).replace(" ", "")


if __name__ == '__main__':
    #main('test3', 'www.test3.com',1,1) 用户,网站,是否301跳转,是否创建mysql
    #python create_web.py testaaa www.testaaa.com 1 1
    main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

