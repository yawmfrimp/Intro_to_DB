import mysql.connector
import sys

try:
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'password',
        database = 'world'
    )
except mysql.connector.Error as e:
    print(e)
    sys.exit()
    
    

mycursor = mydb.cursor()
mycursor.execute('''
CREATE DATABASE IF NOT EXISTS alx_book_store
''')

print('Database \'alx_book_store\' created successfully!')

mycursor.close()
mydb.close()

for i in mycursor:
    print(i)