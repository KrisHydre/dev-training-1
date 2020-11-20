#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:56:05 2020

@author: krish
"""
########################################
## Login the Website By SELENIUM
## and print the Name of the Log-in User
########################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.remote import errorhandler

# Fixing the missing Firefox geckodirver 
# import geckodriver_autoinstaller
# geckodriver_autoinstaller.install()

browser = webdriver.Firefox ()
browser.get ('http://45.79.43.178/source_carts/wordpress/wp-admin/')
username = browser.find_element_by_id("user_login")
username.clear()
username.send_keys("admin")
passwd = browser.find_element_by_id("user_pass")
passwd.clear()
passwd.send_keys("123456aA")
passwd.send_keys(Keys.RETURN)

print ('Please waiting for Website Fully Loading')
a= '*'
sleep (1)
for i in range (6):
    a = a + '*'
    print (a)
    sleep (1)
    
while True:
    try:
        
        a = browser.find_element_by_class_name('display-name')
        print ('The name of the recently log-in user is "{}"'.format (a.text))
        print ('***********************************************')
        break
    except errorhandler.NoSuchElementException:
        continue
