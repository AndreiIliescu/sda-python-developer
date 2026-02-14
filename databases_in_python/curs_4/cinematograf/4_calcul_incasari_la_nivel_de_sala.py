# Incasari la nivel de id de sala

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

with db.cursor() as c:
    select_query = """
        select sala_id, sum(pret) as incasari_totale
        from bilete
        group by sala_id
        order by incasari_totale
    """
    c.execute(select_query)
    results = c.fetchall()

    for r in results:
        print(f"Sala {r[0]} cu suma de {r[1]} RON")
db.close()
