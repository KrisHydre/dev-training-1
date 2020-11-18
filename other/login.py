#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:56:05 2020

@author: krish
"""

######################
#Login by Python  #

# # By REQUEST

# import requests as r
# link = 'http://45.79.43.178/source_carts/wordpress/wp-admin/'
# re = r.get(link, auth=('admin', '12345678aA'))
# print (re.status_code)


# By selenium
from selenium import webdriver


#Fixing the missing Firefox geckodirver 
import geckodriver_autoinstaller
geckodriver_autoinstaller.install()


browser = webdriver.Firefox ()
browser.get ('http://45.79.43.178/source_carts/wordpress/wp-admin/')



