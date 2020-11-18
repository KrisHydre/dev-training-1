#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:21:27 2020

@author: krish
"""
#################################################################
# Get the customer infos from Shopify API by the Trial Account  #
#################################################################

import requests as re
import csv

# Get the customer data from api
link = 'https://thanh-dieu.myshopify.com/admin/api/2020-10/customers.json'
r = re.get(link, auth=('e6eb2b02a65e59f6d42878ddb740a502', \
                  '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'))
a = r.json()

# Convert to csv file and save
a = a['customers']
column = []
for col in a[1].keys():
    column.append (col)

with open ('customer_api.csv', 'w+') as f:
    w = csv.DictWriter(f, fieldnames=column)
    w.writeheader()
    for data in a:
        w.writerow(data)
        
