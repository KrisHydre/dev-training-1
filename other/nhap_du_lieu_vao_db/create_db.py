from time import sleep
import mysql.connector as con
from mysql.connector import errorcode

#######################################
# CREATE THE DATABASE 

## Please re-check the USER and PASSWORD before RUN the code(IN YOUR INPUT)

def login_acc():
# CREATE A CONNECTION WITH MYSQL SERVER
    while True:
        try:
            User = input ('Please type the USERNAME to login MySQL Server\n>>')
            Password = input('And the PASSWORD\n>>')
            connects = con.MySQLConnection(user=User, password=Password,
                             host='127.0.0.1', auth_plugin='mysql_native_password')
            break
        except con.Error as err:
            print ('Fail to connect to MySQL. {}.'.format (err))
            print ('Maybe the user-pass is not true. Please re-consider that.')
            continue
    return User, Password, connects
    
def create_database(connects):
# CREATE A CURSOR & DB   
    while True:   
        try:  
            cursor = connects.cursor()
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
            cursor.close(), connects.close()
            break
        except con.Error as err:
            print (err)
            continue
            
if __name__ == '__main__':
    user, passwd, connects = login_acc()
    create_database()
