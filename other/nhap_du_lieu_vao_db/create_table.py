#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 17:03:08 2020

@author: krish
"""
import mysql.connector as con
from mysql.connector import errorcode
from create_db import *
from time import sleep
import csv, sys
###########################################################
# Please run the create_db.py BEFORE running this scripts #

table = (
    'CREATE TABLE customer ('
    'customer_id INT NOT NULL PRIMARY KEY,'
    'first_name VARCHAR(20),'
    'last_name VARCHAR(20),'
    'company_name VARCHAR(30),'
    'billing_address_1 VARCHAR(30),'
    'billing_address_2 VARCHAR(15),'
    'city VARCHAR(16),'
    'state CHAR(2),'
    'postal_code VARCHAR(12),'
    'country VARCHAR(20),'
    'phone_number VARCHAR(15),'
    'email_address VARCHAR(40),'
    'create_date VARCHAR (30)'
    ')')

insert_values = '''\
    INSERT INTO customer \
VALUES (%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')'''
        
values = []
with open ('customer.csv', 'r') as f:
    r = csv.reader(f, delimiter=',')
    next (r, None)
    for i in r:
        values.append(i)
        
#### CHECKING ALREADY RUNNING THE CREATE DATABASE OR NOT
def checking_db_existing():
    global user, passw, connects
    while True:
        ans = input ('Do you run the code from "create_db.py" ? (Y/n)\n>>').lower()
        if ans == 'y':
            user, passw, connects = login_acc()
            break
        elif ans == 'n':
            user, passw, connects = login_acc()
            create_database(connects) # This function is from 'create_db.py' module
            break
        else:
            print ('Wrong answer please re-type it.')
            continue
        
#### CREATE TABLE AND INSERT THE DATA
def create_table (cursor):
    try:
        cursor.execute (table)
        for val in values:
            cursor.execute(insert_values %(int(val[0]), val[1], val[2], val[3],\
                                               val[4],val[5],val[6], val[7], \
                                                   val[8], val[9], val[10], val[11],val[12]))
    except con.Error as err:
        print ('Failing creating database: {}'.format (err))
        print ('Please reconsider the sources code')
        sys.exit (1)
        
checking_db_existing()
connects  = con.connect(user=user, password=passw, host='127.0.0.1',
                    auth_plugin='mysql_native_password',
                    database='customer_details')
print ('********************************')
sleep (1)
print ('Connecting to MySQL Server...')
sleep(2)
cursor = connects.cursor()
before_create = ['USE customer_details',
        'DROP TABLE IF EXISTS customer']
for i in before_create:
    cursor.execute(i)
print ('********************************')
sleep (1)
print ('Creating the customer table')
sleep (2)
print ('********************************')
sleep (1)
print ('Inserting the customer data')
sleep(1.5)
print ('********************************')
print ('Done............')
create_table(cursor)

# COMMIT THE DATA TO THE DATABASE & AND CLOSE
connects.commit()
cursor.close(), connects.close()
