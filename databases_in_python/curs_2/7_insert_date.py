import mysql.connector as mysql


db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '#t*W3*z5+a77I!P@+173',
    database = 'datacamp'
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
