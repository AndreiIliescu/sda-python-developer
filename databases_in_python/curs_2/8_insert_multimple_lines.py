import mysql.connector as mysql


db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '#t*W3*z5+a77I!P@+173',
    database = 'datacamp'
)

cursor = db.cursor()

query = "insert into users (name, user_name) values (%s, %s)"
values = [
    ("andrei", "andrei26456"),
    ("alex", "alex6156"),
    ("miruna", "miruna8199"),
    ("ioana", "ioana86478")
]

# v1 - execute many
# try:
#     cursor.executemany(query, values)
#     print(f"Au fost inserate {cursor.rowcount} linii.")
#     db.commit()
# except mysql.Error as err:
#     print(f"Eroare: {err}")
# finally:
#     db.close()

# v2 - varinata cu for loop
count = 0

for value in values:
    cursor.execute(query, value)
    count += 1
    print(f'Valoare inserata: {value}')

db.commit()
db.close()
print(f'Au fost inserate {count} linii cu for loop')
