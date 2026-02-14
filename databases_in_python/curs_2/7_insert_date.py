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

# %s = placeholder (loc rezervat pt. date)

query = "insert into users (name, user_name) values (%s, %s)"
values = ("raul", "raul2000")

try:
    cursor.execute(query, values)
    print("Datele au fost inserate")
    db.commit()
except mysql.Error as err:
    print(f"Eroare: {err}")
finally:
    db.close()

# Inchide conexiunea la baza de date: db.close()
