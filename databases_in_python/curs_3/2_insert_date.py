from dotenv import load_dotenv
import os
import mysql.connector as mysql
from fisier_import_date import lista_clienti, lista_filme, lista_sali, lista_bilete


load_dotenv()

db = mysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME_2")
)

with db.cursor() as c:
    insert_clienti = "INSERT INTO clienti (nume, email, telefon, data_nasterii) VALUES (%s, %s, %s, %s)"
    c.executemany(insert_clienti, lista_clienti)
    db.commit()
    print("S-au introdus datele in <clienti>.\n")
    
    insert_filme = "INSERT INTO filme (nume, an_lansare, descriere) VALUES (%s, %s, %s)"
    c.executemany(insert_filme, lista_filme)
    db.commit()
    print("S-au introdus datele in <filme>.\n")
    
    insert_sali = "INSERT INTO sali (denumire, capacitate, vip) VALUES (%s, %s, %s)"
    c.executemany(insert_sali, lista_sali)
    db.commit()
    print("S-au introdus datele in <sali>.\n")
    
    insert_bilete = "INSERT INTO bilete (film_id, client_id, sala_id, pret, data_ora) VALUES (%s, %s, %s, %s, %s)"
    c.executemany(insert_bilete, lista_bilete)
    db.commit()
    print("S-au introdus datele in <bilete>.\n")
