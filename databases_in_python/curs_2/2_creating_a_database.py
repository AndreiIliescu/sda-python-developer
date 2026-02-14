import mysql.connector as mysql


db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '#t*W3*z5+a77I!P@+173'
)

# Crearea unei instante a clasei cursor care este folosita pt. a executa instructiunile SQL in Python
# Cursorul permite interactiunea cu baza de date
cursor = db.cursor()

try:
    cursor.execute("create database datacamp")
    print("Baza de date a fost creata cu succes.")
    
except mysql.Error as err:
    print(f"Eroare: {err}")
