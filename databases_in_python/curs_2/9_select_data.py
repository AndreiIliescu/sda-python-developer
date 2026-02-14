import mysql.connector as mysql


db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '#t*W3*z5+a77I!P@+173',
    database = 'datacamp'
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
