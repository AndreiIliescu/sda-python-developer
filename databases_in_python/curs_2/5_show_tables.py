import mysql.connector as mysql


db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '#t*W3*z5+a77I!P@+173',
    database = 'datacamp'
)

cursor = db.cursor()

cursor.execute("show tables")

tables = cursor.fetchall()
print(f"Aici este lista cu toate tabelele: {tables}")

print()

for table in tables:
    print(table)
