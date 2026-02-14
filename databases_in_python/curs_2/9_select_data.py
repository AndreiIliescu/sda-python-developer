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

# v1
query = 'select * from users'

cursor.execute(query)

records = cursor.fetchall()

print(records)

# v2
for record in records:
    print(record)
    
db.close()
