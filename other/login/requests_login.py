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
    
link = 'http://45.79.43.178/source_carts/wordpress/wp-admin/'
req = r.get(link, auth=('admin', '12345678aA'))

if req.status_code == 200:
    print ('Connect to the Website successfully.')




