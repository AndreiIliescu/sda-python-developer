'''
    1. O sa avem niste utilizatori care trebuie sa aiba neaparat un nume, email, parola.
    2. O sa avem produse pe care utilizatorii le pot cumpara daca sunt disponibile.
    Un produs are denumire, cantitate, pret.

    Inainte sa fie logat utilizatorul:
    1. Log-in (cerem de la utilizator email si parola)
    2. Register (cerem de la utilizator nume, email, parola si ii facem un cont)
    0. Exit application

    Dupa login:
    1. Afiseaza lista de produse disponibile (afisam produsele care au cantitatea > 0)
    2. Cumpara produs (ii cerem un id de produs si o cantitate si daca exista suficienta cantitate
    ii lasam sa cumpere (scade cantitatea de pe produs si se adauga in istoric cumparaturi))
    3. Afiseaza istoric cumparaturi (ii afisam ce produs a cumparat, cand l-a cumparat (data si ora)
    si cat a platit in total (cantitate * pret))
    4. Adaugare produs - denumire, cantitate, pret
    5. Log out - se intoarce la primul meniu
    0. Exit application
'''

# db shop
# utilizator(id, nume, email, parola)
# produs(id, denumire, cantitate, pret)
# istoric(id, user_id, produs_id, data_cumparare, cantitate_cumparata)

import mysql.connector as mysql
import datetime


def create_structure():
    
    db = mysql.connect(
        host = 'localhost',
        user = 'root',
        password = '#t*W3*z5+a77I!P@+173'
    )
    
    with db.cursor() as c:
        try:
            c.execute('create database shop')
            print("Baza de date a fost creata cu succes!")
        except mysql.Error as err:
            print(f'Eroare la crearea bazei de date: {err}!')
            
        c.execute('use shop')
        
        try:
            create_utilizator = '''
                  create table utilizator(
                      id int primary key auto_increment,
                      nume varchar(100) not null,
                      email varchar(100) not null unique,
                      parola varchar(100) not null
                  )
                '''
            c.execute(create_utilizator)
            print('Tabela <~ utilizator ~> a fost creata cu succes!')
        except mysql.Error as err:
            print(f'Eroare la crearea tabelei <~ utilizator ~>: {err}!')

        try:
            create_produs = '''
                  create table produs(
                      id int primary key auto_increment,
                      denumire varchar(255) not null,
                      cantitate int not null,
                      pret double(10, 2) not null
                  )
                '''
            c.execute(create_produs)
            print('Tabela <~ produs ~> a fost creata cu succes!')
        except mysql.Error as err:
            print(f'Eroare la crearea tabelei <~ produs ~>: {err}!')
            
        try:
            create_istoric = '''
                  create table istoric(
                      id int primary key auto_increment,
                      user_id int not null,
                      produs_id int not null,
                      data_cumparare timestamp not null,
                      cantitate_cumparata int not null,
                      foreign key (user_id) references utilizator(id),
                      foreign key (produs_id) references produs(id)
                  )
                '''
            c.execute(create_istoric)
            print('Tabela <~ istoric ~> a fost creata cu succes!')
        except mysql.Error as err:
            print(f'Eroare la crearea tabelei <~ istoric ~>: {err}!')


create_structure()

def show_menu_1():
    print("1. Log-in")
    print("2. Register")
    print("0. Exit application")


def show_menu_2():
    print("1. Afiseaza lista de produse disponibile")
    print("2. Cumpara produs")
    print("3. Afiseaza istoric cumparaturi si cat a platit in total")
    print("4. Adaugare produs")
    print("5. Log out")
    print("0. Exit application")
    
    
db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '#t*W3*z5+a77I!P@+173',
    database = 'shop'
)

user_logat = None

while True:
    if user_logat is None:
        show_menu_1()
        
        option = int(input("Select an option: "))
        
        if option == 0:
            break
        elif option == 1:
            email = input("Type your email: ")
            password = input("Type your password: ")
        
            with db.cursor() as c:
                c.execute("""
                          select id
                          from utilizator
                          where email = %s and parola = %s
                          """, (email, password))
                
                result = c.fetchone()
                
                if result:
                    user_logat = result[0]
                    print("Authentication successful.")
                else:
                    print("Invalid email or password.")
                    
        elif option == 2:
            name = input("Type your username: ")
            email = input("Type your email: ")
            password = input("Type your password: ")
            
            with db.cursor() as c:
                c.execute('''
                          insert into utilizator (nume, email, parola) 
                          values (%s, %s, %s)
                          ''', (name, email, password))
                
                db.commit()
                
    else:
        show_menu_2()
        
        option = int(input("Type your option: "))
        
        if option == 0:
            break
        elif option == 1:
                with db.cursor() as c:
                    c.execute("select * from produs where cantitate > 0")
                    
                    produse = c.fetchall()
                    
                    print("_" * 30)
                    print("Lista de produse:")
                    
                    for produs in produse:
                        print(f"Produsul {produs[1]} cu id-ul {produs[0]} are cantitatea {produs[2]} si pretul {produs[3]} RON.")
                        
                    print("_" * 30)
                    
        elif option == 2:
            product_id = int(input("Introduceti ID produs: "))
            quantity = int(input("Introduceti cantitatea: "))
            
            with db.cursor() as c:
                c.execute(
                    """
                    select * from produs where id = %s and cantitate >= %s
                    """, (product_id, quantity))
                
                result = c.fetchone()

                if result:
                    c.execute("update produs set cantitate = cantitate - %s where id = %s", (quantity, product_id))
                    c.execute("insert into istoric (user_id, produs_id, data_cumparare, cantitate_cumparata) values (%s, %s, %s, %s)",
                              (user_logat, product_id, datetime.datetime.now(), quantity))
                    
                    db.commit()
                    print("Comanda a fost exectuata cu succes!")
                
                else:
                    print("Nu exista produsul sau cantitatea suficienta.")
                    
        elif option == 3:
            # denumire produs, valoare totala achizitie produs, data cumparare produs
            with db.cursor as c:
                c.execute(
                    """
                    select denumire, data_cumparare,
                    (cantitate_cumparata * pret) valoare_totala_achizitie_produs
                    from istoric i
                    join produs p on i.produs_id = p.id
                    where user_id = %s
                    """, (user_logat,)
                )
                
                results = c.fetchall()
                
                print("Istoric cumparaturi:")
                
                for result in results:
                    print(f"Ati cumparat {result[0]} in valoare de {result[1]} RON in data de {result[2]}")
                    
                print("_" * 20)
                    
        elif option == 4:
            denumire = input("Denumire: ")
            cantitate = int(input("Cantitate: "))
            pret = float(input("Pret: "))
            
            with db.cursor() as c:
                c.execute("""
                          insert into produs (denumire, cantitate, pret)
                          values (%s, %s, %s)
                          """, (denumire, cantitate, pret))
                
                db.commit()
                print("Produs adaugat cu succes.")
                
        elif option == 5:
            user_logat = None
            print("Te-am scos boss.")

db.close()
