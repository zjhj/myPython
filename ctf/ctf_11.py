#! /usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

res = list()

for i in itertools.permutations( [1,2,3,4,5,6,7,8,9,10],10 ):
    a1 = i[0]+i[1]+i[2]
    a2 = i[3]+i[2]+i[7]
    a3 = i[8]+i[7]+i[6]
    a4 = i[9]+i[6]+i[4]
    a5 = i[5]+i[4]+i[1]
    if a1 == a2 and a1==a3 and a1==a4 and a1==a5:
        res.append( str(i[0]) + str(i[1]) + str(i[2]) + str(i[3]) + str(i[2]) + str(i[7]) + str(i[8]) + str(i[7]) + str(i[6]) + str(i[9]) + str(i[6]) + str(i[4]) + str(i[5]) + str(i[4]) + str(i[1]) )

import pycurl
from urllib import urlencode
from io import BytesIO

buffer = BytesIO()

c = pycurl.Curl()
c.setopt( c.URL, 'http://ctf5.shiyanbar.com/program/2/check.php' )
c.setopt( c.WRITEFUNCTION, buffer.write )

for i in res:
    buffer = BytesIO()
    c.setopt( c.POSTFIELDS, urlencode( {'answer':i,'submit':'我要key'} ) )
    c.perform()

    if len( buffer.getvalue() ) != 11:
        print i, buffer.getvalue().decode( 'gbk' )
        break
c.close()

# print buffer.getvalue().decode( 'gbk' )
# print len( buffer.getvalue() )

"""
import os
for i in res:
    ret = os.popen( 'curl -d "answer=' + i + '&submit=我要KEY" "http://ctf5.shiyanbar.com/program/2/check.php"' ).read()
    if len( ret ) != 11:
        print i,ret
        break
"""
