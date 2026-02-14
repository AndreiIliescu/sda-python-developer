import mysql.connector as mysql
import pandas as pd


def export_to_excel():
    db = mysql.connect(
        host = 'localhost',
        user = 'root',
        password = '#t*W3*z5+a77I!P@+173',
        database = 'tasks'
    )
    
    with db.cursor() as c:
        c.execute("select * from tasks order by id")
        results = c.fetchall()
        
    df = pd.DataFrame(results, columns=['ID', 'Task', 'Done'])
    
    # Index  = False, adica ii spunem pui Pandas ca nu este nevoie sa indexeze el automat randurile cu date
    df.to_excel('tasks.xlsx', index=False)
    
    db.close()
    
    
export_to_excel()
