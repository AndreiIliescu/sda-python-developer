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

cursor.execute("show tables")

tables = cursor.fetchall()
print(f"Aici este lista cu toate tabelele: {tables}")

print()

for table in tables:
    print(table)
