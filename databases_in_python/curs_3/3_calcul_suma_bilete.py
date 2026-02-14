from dotenv import load_dotenv
import os
import mysql.connector as mysql


load_dotenv()

db = mysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME_2")
)

# Cati bani s-au facut in anul 2021 pe filmul cu id 1
# SELECT SUM(nume coloana pe care vrem sa facem suma) FROM tabela ...
with db.cursor() as c:
    select_query = '''
                SELECT SUM(pret)
                FROM bilete
                WHERE film_id = 1 AND YEAR(data_ora) = 2021
    '''
    c.execute(select_query)
    incasari_film = c.fetchone()
    print(f"Rezultat: {incasari_film[0]}")

# with db.cursor() as c:
#     select_query = '''
#                 SELECT SUM(pret)
#                 FROM bilete
#                 WHERE film_id = %s AND YEAR(data_ora) = %s
#     '''
#     c.execute(select_query, (1, 2021))
#     incasari_film = c.fetchone()
#     print(f"Rezultat: {incasari_film[0]}")
