import mysql.connector as mysql


db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '#t*W3*z5+a77I!P@+173'
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
