# Vom crea o aplicatie pt. task-uri
# 4 optiuni: show tasks, mark task as done, add new task, exit
# Baza de date tasks
# Table task

from dotenv import load_dotenv
import os
import mysql.connector as mysql


load_dotenv()

# Vom crea o functie de creare a structurii bazei de date
# Unde vom defini conexiunea si vom executa scripturile de creare a bazei de date si a tabelei
def create_structure():
    db = mysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )
    
    # baza de date
    with db.cursor() as c:
        try:
            c.execute("CREATE DATABASE tasks")
            print("Baza de date a fost creata cu succes!")
        except mysql.Error as err:
            print(f"Eroare la creare bazei de date: {err}")
    db.close()

    db = mysql.connect(
        host = 'localhost',
        user = 'root',
        password = '#t*W3*z5+a77I!P@+173',
        database = 'tasks'
    )

    # tasks(id, task, done)
    with db.cursor() as c:
        try:
            try:
                create_tasks = """
                create table tasks(
                    id int primary key auto_increment,
                    task varchar(255) not null,
                    done boolean not null default false
                )
                """
                c.execute(create_tasks)
                print("Tabela a fost creata!")
                
            except mysql.Error as err:
                print(f"Eroare: {err}")
        except mysql.Error as err:
            print(f"Eroare la crearea tabelei: {err}")
    db.close()


create_structure()

def show_menu():
    print("1. Show task")
    print("2. Mark task as done")
    print("3. Add new task")
    print("0. Exit")

def show_tasks():
    db = mysql.connect(
        host = 'localhost',
        user = 'root',
        password = '#t*W3*z5+a77I!P@+173',
        database = 'tasks'
    )

    with db.cursor() as c:
        select_query = '''
            select *
            from tasks
            where done = false
            order by id
        '''
        c.execute(select_query)
        results = c.fetchall()
        
        if results is not None:
            for r in results:
                print(r[1])
                print(f'task_id: {r[0]} - name: {r[1]} - status: {r[2]}')
        else:
            print("Nu avem task-uri realizate.")

# Mark task as done
def mark_task_as_done():
    db = mysql.connect(
        host = 'localhost',
        user = 'root',
        password = '#t*W3*z5+a77I!P@+173',
        database = 'tasks'
    )
    
    choice = int(input("Enter completed task id: "))
    with db.cursor() as c:
        c.execute("""
                  update tasks set done = 'true'
                  where id = %s
                  """, (choice,))
        db.commit()
        print(f"Task-ul cu id {choice} a fost actualizat.")
        

def add_task():
    db = mysql.connect(
        host = 'localhost',
        user = 'root',
        password = '#t*W3*z5+a77I!P@+173',
        database = 'tasks'
    )
    
    task_name = input("Insert task name: ")
    with db.cursor() as c:
        c.execute("""
                  insert into tasks (task)
                  values (%s)
                  """, (task_name,))
        db.commit()
        print(f"Task-ul {task_name} a fost adaugat.")
        

while True:
    show_menu()
    choice = int(input("Enter choice: "))
    if choice == 0:
        print("La revedere!")
        break
    elif choice == 1:
        show_tasks()
    elif choice == 2:
        mark_task_as_done()
    elif choice == 3:
        add_task()
    else:
        print("Invalid option. Please select a valid option from the menu!")
