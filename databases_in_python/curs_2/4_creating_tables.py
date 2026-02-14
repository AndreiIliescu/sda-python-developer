'''
users (name, user_name)
'''

from dotenv import load_dotenv
import os
import mysql.connector as mysql


load_dotenv()

db = mysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
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
