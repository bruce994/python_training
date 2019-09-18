#!/usr/bin/python
#encoding=utf8

import os
import sys
import urllib
import urllib2
import json
import hashlib
import hmac
import time
import datetime
from urllib import quote
from urlparse import urlparse
import MySQLdb


def to_utf8(text):
    if isinstance(text, unicode):
        # unicode to utf-8
        return text.encode('utf-8')
    try:
        # maybe utf-8
        return text.decode('utf-8').encode('utf-8')
    except UnicodeError:
        # gbk to utf-8
        return text.decode('gbk').encode('utf-8')


def gen_auth(access_key, secret_key, utc_time_str, url, method):
    url_parse_ret = urlparse(url)
    host = url_parse_ret.hostname
    path = url_parse_ret.path
    version = "1"
    expiration_seconds = "1800"
    signature_headers = "host"

    # 1 Generate SigningKey
    val = "bce-auth-v%s/%s/%s/%s" % (version, access_key, utc_time_str, expiration_seconds)
    signing_key = hmac.new(secret_key, val, hashlib.sha256).hexdigest().encode('utf-8')

    # 2 Generate CanonicalRequest
    # 2.1 Genrate CanonicalURI
    canonical_uri = quote(path)
    # 2.2 Generate CanonicalURI: not used here
    # 2.3 Generate CanonicalHeaders: only include host here
    canonical_headers = "host:%s" % quote(host).strip()
    # 2.4 Generate CanonicalRequest
    canonical_request = "%s\n%s\n\n%s" % (method.upper(), canonical_uri, canonical_headers)

    # 3 Generate Final Signature
    signature = hmac.new(signing_key, canonical_request, hashlib.sha256).hexdigest()
    authorization = "bce-auth-v%s/%s/%s/%s/%s/%s" % (version, access_key, utc_time_str, expiration_seconds, signature_headers, signature)
    print authorization
    return authorization

if __name__ == "__main__":
    access_key = "be5ffd375a69434eada1203ed4400e02"
    secret_key = "2b4a40343614482bad2a0b5f13b2d46c"

    conn = MySQLdb.connect(host='sh-cdb-qenvqae8.sql.tencentcdb.com',port=63986,user='a_20190912',passwd='Qs!CEcxgqP2nqcq',db='20190912',charset='utf8', init_command='SET NAMES UTF8')
    cursor = conn.cursor()
    cursor.execute("select eqid,e_status,id from tp_form WHERE eqid<>'' AND e_status=0 ")

    for row in cursor.fetchall():
        eqid = row[0]
        id = row[2]

        #eqid="e07bde4900175154000000065d808885"
        url = "http://referer.bj.baidubce.com/v1/eqid"+"/"+eqid
        method = "GET"
        utc_time = datetime.datetime.utcnow()
        utc_time_str = utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")
        auth = gen_auth(access_key, secret_key, utc_time_str, url, method)

        header = {
                'accept-encoding':'gzip, deflate',
                'host':'referer.bj.baidubce.com',
                'content-type':'application/json',
                'x-bce-date': utc_time_str,
                'authorization': auth,
                'accept':'*/*'
        }

        print time.time()
        request = urllib2.Request(url, None, header)
        response = None
        try :
                response = urllib2.urlopen(request)
                print time.time()
                post_res_str = response.read()
                print post_res_str
                pp = json.loads(post_res_str)
                keyword = urllib.unquote(to_utf8(pp['wd']))
                sql = "update tp_form set keyword='{}',e_status=1 WHERE id={}".format(keyword,id)
                print sql
                cursor.execute(sql)
                conn.commit()

        except urllib2.URLError, e:
                print "URLError"
                print e.code, e.reason
                print e.read()
        except urllib2.HTTPError, e:
                print "HTTPError"
                print e.code, e.reason
                print e.read()
                
