import mysql.connector as con
from mysql.connector import errorcode
from create_db import *
from time import sleep
##########################################################
# Please run the create_db.py BEFORE running this scripts

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
insert_values = (
"INSERT INTO customer "
"(customer_id, first_name, last_name, company_name, billing_address_1, billing_address_2, city, state, postal_code, country, phone_number, email_address, create_date)"
" VALUES"
"(69906,'justin','arsenault','','732 eastford rd','','Southbridge','MA','1550','United States','508-735-9694','hondarider2508@gmail.com','10-01-19 06:47 AM'),"
"(69907,'Wade','Banks','','606 Ridge Way','','Evans','GA','30809','United States','706-836-3122','bankswade77@gmail.com','10-01-19 07:03 AM'),"
"(69908,'Sean','Powers','','293 ROSENSTEEL RD','','SALTSBURG','PA','15681','United States','7244647895','bonez62@netzero.com','10-01-19 07:31 AM'),"
"(69909,'Riley','Cocke','Western counters','1008 18th st','4','Paso Robles','CA','93446','United States','8059752151','dailydriven90ls@gmail.com','10-01-19 08:27 AM'),"
"(69910,'Sherrilyn','Carroll','','12008 238TH AVE E','','BUCKLEY','WA','98321-9680','United States','3608970890','action@centurytel.net','10-01-19 08:51 AM'),"
"(69911,'Rickey','Johnson','','144 Velvet Ridge Rd','','BRADFORD','AR','72020','United States','15012780369','rjgalute@gmail.com','10-01-19 09:34 AM'),"
"(69912,'Sandra','Lemunyon','Low Kountry Trukkin','6123 Warner rd','','Columbus','GA','31909','United States','3363546684','Crazyred1992@outlook.com','10-01-19 09:43 AM'),"
"(69913,'Thomas','Campbell','','22875 Bravo Place','','Salinas','CA','93908','United States','8318097979','Soup5511@gmail.com','10-01-19 10:44 AM'),"
"(69914,'Tom','Crenshaw','','228 Florence Dr','','Aptof','CA','95003','United States','831-431-0906','tomcrencat@gmail.com','10-01-19 10:49 AM'),"
"(69915,'John','Lowery','1967','897 S ROOSEVELT ROAD J','PORTALES','PORTALES','NM','88130','United States','5752658263','johnlowery67@msn.com','10-01-19 10:49 AM'),"
"(69916,'Stephen','Schroeder','','2078 Butte St','','Redding','CA','96001','United States','210-421-6098','stephencschroeder@sbcglobal.net','10-01-19 11:29 AM'),"
"(69917,'Vincent','Loesch','','1125 Minnesota St','','Shakopee','MN','55379','United States','6125584360','vloesch@comcast.net','10-01-19 11:50 AM'),"
"(69918,'Timothy','Pickering','','166 Capron Farm Dr','','Warwick','RI','2886','United States','401-533-6677','timepick67@gmail.com','10-01-19 12:16 PM'),"
"(69919,'Matthew','Gangne','','167 Brickyard Rd.','','Southampton','MA','1073','United States','413-326-1338','electricmatt@yahoo.com','10-01-19 12:18 PM'),"
"(69920,'Jeff','','','','','','','','','','justjeffnv@gmail.com','10-01-19 12:57 PM'),"
"(69921,'James','Sharp','James','5318 Acorn ct','','League City','TX','77573','United States','2817281319','jrsharp1955@comcast.net','10-01-19 01:04 PM'),"
"(69922,'Lucas','Walker','','6477 Bayou Glen Rd.','','Houston','TX','77057','United States','2108627702','lhwalker.cl300@hotmail.com','10-01-19 01:14 PM'),"
"(69923,'pierre andre','martel','','10 DE BRAINE','','BLAINVILLE','QC','j7b1z1','Canada','514-629-0849','pierre-andremartel@hotmail.com','10-01-19 01:32 PM')"
)

def checking_db_existing():
    global user, passw, conn
    while True:
        ans = input ('Do you run the code from "create_db.py" ? (Y/n)\n>>').lower()
        if ans == 'y':
            user, passw, conn = login_acc()
            break
        elif ans == 'n':
            user, passw, conn = login_acc()
            create_database()
            break
        else:
            print ('Wrong answer please re-type it.')
            continue
        
#### CREATE TABLE AND INSERT THE DATA ###
def create_table (cursor):
    try:
        cursor.execute (table)
        cursor.execute (insert_values)
    except con.Error as err:
        print ('Failing creating database: {}'.format (err))
        exit (1)


    


checking_db_existing()
conn  = con.connect(user=user, password=passw, host='127.0.0.1',
                    auth_plugin='mysql_native_password',
                    database='customer_details')
print ('********************************')
sleep (1)
print ('Connecting to MySQL Server...')
sleep(2)
cursor = conn.cursor()
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
conn.commit()
cursor.close(), conn.close()

