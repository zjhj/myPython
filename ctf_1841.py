#! /usr/bin/env python
#  -*- coding:utf-8 -*-

import pycurl
import BeautifulSoup
import hashlib
from StringIO import StringIO
from urllib import urlencode

res = dict()
for i in range(0,100001):
    res[hashlib.sha1( hashlib.md5(str(i)).hexdigest() ).hexdigest()] = i

buffer = StringIO()
c = pycurl.Curl()
c.setopt( pycurl.URL, "http://ctf5.shiyanbar.com/ppc/sd.php" )
c.setopt( pycurl.WRITEDATA, buffer )
c.setopt( pycurl.COOKIEJAR, "cookie_test.txt" )

c.perform()
c.close()

soup = BeautifulSoup.BeautifulSoup( buffer.getvalue() )
curr_res = soup.find( "div" ).contents[0]

del c
del buffer

buffer = StringIO()
post_data = {'inputNumber': res[curr_res],'submit':'提交'}

c = pycurl.Curl()
c.setopt( pycurl.URL, "http://ctf5.shiyanbar.com/ppc/sd.php" )
c.setopt( pycurl.WRITEDATA, buffer )
c.setopt( pycurl.COOKIEFILE, "cookie_test.txt" )
c.setopt( pycurl.POSTFIELDS, urlencode(post_data) )
c.perform()
c.close()

print buffer.getvalue()
