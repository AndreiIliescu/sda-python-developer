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

cursor.execute("show databases")

'''
fetchone() - ne afiseaza un singur rezultat
fetchall() - afiseaza toate rezultatele
fetchmany() - afiseaza cate date dorim (5) - afiseaza primele 5 date
'''

databases = cursor.fetchall()

print(f"Aici este lista cu toate bazele de date: {databases}")
print(type(databases))

print()

for data in databases:
    print(databases)
