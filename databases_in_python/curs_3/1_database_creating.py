# Vom avea o baza de date pt. un cinematograf
# Vom crea tabelele:
# clienti (id, nume, email, telefon, data_nasterii)
# filme (id, nume, an_lasare, descriere)
# sali (id, denumire, capacitate, vip)
# bilete (id, film_id, client_id, sala_id, pret, data_ora)

import mysql.connector as mysql


db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '#t*W3*z5+a77I!P@+173',
)

# "with" este folosit pt. a gestiona automat resursele (cursorul)
with db.cursor() as c:
    try:
        c.execute("CREATE DATABASE cinematograf")
        print("Baza de date <cinematograf> a fost creata fara probleme!\n")
        
    except mysql.Error as err:
        print(f"Eroare creare baza de date: {err}")

# Creati conexiunea completa cu noua baza completa
# Creati tabela clienti (id, nume, email, telefon, data_nasterii)
db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '#t*W3*z5+a77I!P@+173',
    database = 'cinematograf'
)

with db.cursor() as c:
    try:
        try:
            create_clienti = '''
            CREATE TABLE clienti(
                id INT PRIMARY KEY AUTO_INCREMENT,
                nume VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE,
                telefon VARCHAR(20),
                data_nasterii DATE NOT NULL
            )
            '''
            c.execute(create_clienti)
            print("Tabela <clienti> a fost creata fara probleme!\n")
            
        except mysql.Error as err:
            print(f"Eroare: {err}")

        # filme (id, nume, an_lansare, descriere)
        try:
            create_filme = '''
            CREATE TABLE filme(
                id INT PRIMARY KEY AUTO_INCREMENT,
                nume VARCHAR(100) NOT NULL,
                an_lansare INT NOT NULL,
                descriere LONGTEXT NOT NULL
            )
            '''
            c.execute(create_filme)
            print("Tabela <filme> a fost creata fara probleme!\n")
            
        except mysql.Error as err:
            print(f"Eroare: {err}")

        # sali (id, denumire, capacitate, vip)
        try:
            create_sali = '''
            CREATE TABLE sali(
                id INT PRIMARY KEY AUTO_INCREMENT,
                denumire VARCHAR(20) NOT NULL,
                capacitate INT,
                vip BOOLEAN
            )
            '''
            c.execute(create_sali)
            print("Tabela <sali> a fost creata fara probleme!\n")
            
        except mysql.Error as err:
            print(f"Eroare: {err}")
            
        # bilete (id, film_id, client_id, sala_id, pret, data_ora)
        try:
            create_bilete = '''
            CREATE TABLE bilete(
                id INT PRIMARY KEY AUTO_INCREMENT,
                film_id INT NOT NULL,
                client_id INT NOT NULL,
                sala_id INT NOT NULL,
                pret DOUBLE(4, 2) NOT NULL,
                data_ora DATETIME NOT NULL,
                FOREIGN KEY (film_id) REFERENCES filme(id),
                FOREIGN KEY (client_id) REFERENCES clienti(id),
                FOREIGN KEY (sala_id) REFERENCES sali(id)
            )
            '''
            c.execute(create_bilete)
            print("Tabela <bilete> a fost creata fara probleme!\n")
            
        except mysql.Error as err:
            print(f"Eroare: {err}")
            
    except mysql.Error as err:
        print(f"Eroare creare tabele: {err}")
