from time import sleep
import mysql.connector as con
from mysql.connector import errorcode

#######################################
# CREATE THE DATABASE 

## Please re-check the USER and PASSWORD before RUN the code

def login_acc():
    # CREATE A CONNECTION WITH MYSQL SERVER
    while True:
        try:
            User = input ('Please type the user name to login MySQL Server\n>>')
            Password = input('And the password\n>>')
            conn = con.MySQLConnection(user=User, password=Password,
                             host='127.0.0.1', auth_plugin='mysql_native_password')
            break
        except mysql.connector.errorcode as err:
            print ('Fail to connect to MySQL. {}.'.format (err))
            continue
    return User, Password, conn
    
def create_database():
# CREATE A CURSOR & DB   
    while True:   
        try:  
            cursor = conn.cursor()
            create_db = [
                'DROP DATABASE IF EXISTS customer_details',
                'CREATE DATABASE customer_details']
            for i in create_db:
                cursor.execute (i)
            sleep(0.75)
            print ('***************************')
            print ('Create the database')
            sleep(2)
            print ('Create schema successfully !')
            cursor.close(), conn.close()
            break
        except mysql.connector.errorcode as err:
            print (err)
            continue
            
if __name__ == '__main__':
    user, passwd, conn = login_acc()
    create_database()
