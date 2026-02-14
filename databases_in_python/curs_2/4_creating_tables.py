'''
users (name, user_name)
'''

import mysql.connector as mysql


db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '#t*W3*z5+a77I!P@+173',
    database = 'datacamp'
)

cursor = db.cursor()

try:
    cursor.execute('''
                   create table if not exists users (
                       name varchar(255),
                       user_name varchar(255)
                   )
                   ''')
    print("Tabela a fost creata")
except mysql.Error as err:
    print(f"Eroare: {err}")
