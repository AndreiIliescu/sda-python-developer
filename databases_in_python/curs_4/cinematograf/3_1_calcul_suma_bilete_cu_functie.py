from dotenv import load_dotenv
import os
import mysql.connector as mysql


load_dotenv()

def calculate_incasare(film_id, year):
    db = mysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME_2")
    )

    with db.cursor() as c:
        select_query = '''
                    SELECT SUM(pret)
                    FROM bilete
                    WHERE film_id = %s AND YEAR(data_ora) = %s
        '''
        c.execute(select_query, (film_id, year))
        incasari_film = c.fetchone()

        if incasari_film and incasari_film[0] is not None:
            print(f"Total incasari pt. filmul cu id {film_id} din anul {year}: {incasari_film[0]} RON")
        else:
            print(f"Nicio incasare pt. filmul cu id {film_id} din anul {year}")
    db.close()
    

calculate_incasare(1, 2021)
calculate_incasare(4, 2025)
calculate_incasare(3, 2020)
