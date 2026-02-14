import mysql.connector as mysql


db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '#t*W3*z5+a77I!P@+173',
    database = 'datacamp'
)

cursor = db.cursor()

# v1
# cursor.execute("describe users")

# print(f"Toata tabela: {cursor.fetchall()}")

# v2
# cursor.execute("describe users")

# for column in cursor:
#     print(column)

# v3
# cursor.execute("describe users")

# for column in cursor:
#     print(f"{column[0]} - {column[1]}")

# v4

cursor.execute("describe users")

for column in cursor:
    name, type, null, key, default, extra = column
    print(f'{name}, {type}, {null}, {key}, {default}, {extra}')
