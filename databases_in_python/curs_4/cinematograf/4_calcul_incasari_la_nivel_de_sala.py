# Incasari la nivel de id de sala

import mysql.connector as mysql


db = mysql.connect(
    host='localhost',
    user='root',
    password='#t*W3*z5+a77I!P@+173',
    database='cinematograf'
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
