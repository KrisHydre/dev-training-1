#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:56:05 2020

@author: krish
"""
######################
#Login by REQUESTS   #
######################

import requests as r
from time import sleep

print ('Connecting..')
for i in range (3):
    print ('.')
    sleep(1)
    
login = 'http://45.79.43.178/source_carts/wordpress/wp-login.php'
link = 'http://45.79.43.178/source_carts/wordpress/wp-admin/'
username = 'admin'
password = '123456aA'
with r.Session() as req:
    datas = {'log':username, 'pwd':password, 'wp-submit':'Log in',
            'redirect_to':link,'testcookie':'1'}
    req.post(login, data = datas)
    resp = req.get (link)
    

if resp.status_code == 200:
    print ('Connect to the Website successfully.')
header = resp.headers
with open ('headers.txt', 'w+') as f:
    f.truncate()
    for x,y in header.items():
        f.writelines ('{}: {}'.format(x,y))
        f.writelines('\n')
txt = resp.text

with open ('text.html', 'w+') as t:
    t.truncate()
    t.write(txt)



