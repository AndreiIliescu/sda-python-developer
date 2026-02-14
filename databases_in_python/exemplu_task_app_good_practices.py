# vom crea o aplicatie pentru task-uri
# 4 optiuni: show tasks, mark task as done, add new task, exit
# baza de date tasks
# tabela task

import mysql.connector as mysql

# vom crea o functie de creare a structurii bazei de date
# unde vom defini conexiunea si vom executa scripturile de creare a bazei de date si a tabelei

def create_structure():
    db = mysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'password'
    )
    
    with db.cursor() as c:
        try:
            c.execute('create database db_tasks')
            print("Baza de date tasks a fost creata.")
        except mysql.Error as err:
            print(f'eroare: {err}')
            
        c.execute('use db_tasks')
        
        try:
            c.execute('''
                  create table tasks(
                      id int primary key auto_increment,
                      task varchar(255) not null,
                      done boolean not null default 0
                  )
                  ''')
            print("Tabela tasks a fost creata cu succes.")
        except mysql.Error as err:
            print(f'eroare: {err}')

# create_structure()
def show_menu():
    print("1. Show task")
    print("2. Mark task as done")
    print("3. Add new task")
    print("0. Exit")

db = mysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'password',
        database = 'db_tasks'
    )

    
def show_tasks():
    with db.cursor() as c:
        c.execute("""
                  select * from tasks where done = 0
                  order by id
                  """)
        results = c.fetchall()
        # [(0, ia paine, 0), (1, ia apa, 0), (2, baga motorina, 0)]
        
        if results is not None:
            for r in results:
                # (0, 'ia paine', 0)
                # (1, 'ia apa', 0)
                # (2, 'baga motorina', 0)
                # #0      1           2
                print(f'task_id: {r[0]} - name: {r[1]} - status: {r[2]}')
        else:
            print("Nu avem task-uri nefinalizate")
            
# mark task as done
def mark_task_as_done():
    choice = int(input("Enter completed task id: "))
    with db.cursor() as c:
        c.execute('''
                  update tasks set done = 1
                  where id = %s
                  ''', (choice,))
        db.commit()
        print(f"Task-ul cu id {choice} a fost actualizat.")
        
        
def add_task():
    task_name = input("Insert task name: ")
    with db.cursor() as c:
        c.execute("""
                  insert into tasks (task)
                  values (%s)
                  """, (task_name,))
        
        db.commit()
        
while True:
    show_menu()
    choice = int(input("Enter choice: "))
    if choice == 0:
        print("La revedere")
        break
    elif choice == 1:
        show_tasks()
    elif choice == 2:
        mark_task_as_done()
    elif choice == 3:
        add_task()
    else:
        print("Invalid option. Please select a valid option.")
