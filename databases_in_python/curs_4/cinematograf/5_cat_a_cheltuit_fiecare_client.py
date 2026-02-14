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

# cat a cheltuit fiecare client
# sumele cheltuite si NUMELE clientului cu pricina
with db.cursor() as c:
    select_query = """
        select nume, sum(pret) total_cheltuit
        from bilete b
        join clienti c
        on b.client_id = c.id
        group by c.id, nume
    """
    c.execute(select_query)
    results = c.fetchall()

    for result in results:
        print(f"{result[0]} a cheltuit {result[1]} RON.")
db.close()
