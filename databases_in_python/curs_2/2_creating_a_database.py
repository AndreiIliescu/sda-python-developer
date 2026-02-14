from dotenv import load_dotenv
import os
import mysql.connector as mysql


load_dotenv()

db = mysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)

# Crearea unei instante a clasei cursor care este folosita pt. a executa instructiunile SQL in Python
# Cursorul permite interactiunea cu baza de date
cursor = db.cursor()

try:
    cursor.execute("create database datacamp")
    print("Baza de date a fost creata cu succes.")
    
except mysql.Error as err:
    print(f"Eroare: {err}")
