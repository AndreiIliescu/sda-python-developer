from dotenv import load_dotenv
import os
import mysql.connector as mysql
import pandas as pd


load_dotenv()

def export_to_excel():
    db = mysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME_3")
    )
    
    with db.cursor() as c:
        c.execute("select * from tasks order by id")
        results = c.fetchall()
        
    df = pd.DataFrame(results, columns=['ID', 'Task', 'Done'])
    
    # Index  = False, adica ii spunem pui Pandas ca nu este nevoie sa indexeze el automat randurile cu date
    df.to_excel('tasks.xlsx', index=False)
    
    db.close()
    
    
export_to_excel()
