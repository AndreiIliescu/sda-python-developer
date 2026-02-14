import mysql.connector as mysql


db = mysql.connect(
    host='localhost',
    user='root',
    password='#t*W3*z5+a77I!P@+173',
    database='cinematograf'
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
