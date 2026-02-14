# CRUD in SQL
# Create = Insert
# Read = Select
# Update = Update
# Delete = Delete

# sqlalchemy
# sqlalchemy-orm

# create_engine - creaza conexiune cu baza de date
# Column, Integer, String - sunt tipuri de coloane
# declarative_base - baza pt. definirea claselor
# sessionmaker - util pt. a creasesiuni de lucru cu baza de date

from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base, sessionmaker


# =================================
# Configurare baza de date
# =================================

def create_database():
    
    temp_engine = create_engine('mysql+pymysql://root:#t*W3*z5+a77I!P%40+173@localhost:3306')
    
    with temp_engine.connect() as connection:
        result = connection.execute(text("show databases like 'students_db'"))
        
        if not result.fetchone():
            connection.execute(text("create database students_db"))
            
            print("Baza de date 'students_db' a fost creata.")
            
        else:
            print("Baza de date 'student_db' exista deja.")
            
create_database()

Base = declarative_base()

engine = create_engine('mysql+pymysql://root:#t*W3*z5+a77I!P%40+173@localhost:3306/students_db')

Session = sessionmaker(bind=engine)
session = Session()

class Student(Base):
    __tablename__ = 'students'
    
    # coloana id, de tip int, primary key
    id = Column(Integer, primary_key=True)
    
    # coloana name, de tip varchar(100), not null
    name = Column(String(100), nullable=False)
    
    # coloana email, de tip varchar(100), not null, unique
    email = Column(String(100), nullable=False, unique=True)
    
    # metoda prin care defineste cum va fi afisat un obiect
    def __repr__(self):
        return f"Student_id: {self.id} - Student_name: {self.name} - Student_email: {self.email}"
    
    
def create_db():
    Base.metadata.create_all(engine)
    print("Tablea Students a fost creata cu succes.")
    

def add_student(name, email):
    student = Student(name=name, email=email)
    session.add(student)
    session.commit()
    print(f"Student {name} cu email-ul {email} a fost adaugat.")
    
    
def list_students():
    students = session.query(Student).all()
    
    if not students:
        print("Nu exista studenti in tabela")
    else:
        for s in students:
            print(f"{s.id} - {s.name} - {s.email}")
            
            
def update_student(student_id, new_name=None, new_email=None):
    '''
    update student - avem nevoie de id-ul studentului si de 2 variabile pt. nume si email
    '''
    
    student = session.query(Student).filter_by(id=student_id).first()
    print(f"Aici este studentul {student}")
    
    if not student:
        print("Studentul nu a fost gasit.")
        return        # punem un return simplu, fara variabila sau altceva, fiindca in cazul in care nu gasim vreun student,
                      # functia sa se opreasca imediat
    
    if new_name:
        student.name = new_name
    
    if new_email:
        student.email = new_email
        
    session.commit()
    
    print(f"Datele studentului cu id-u; {student_id} u fost actualizate.")


def delete_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    
    if not student:
        print("Studentul nu a fost gasit")
        return
    
    session.delete(student)
    session.commit()
    
    print(f"Studentul cu id-ul {student_id} a fost sters.")
    
    
def search_by_name(nume_cautat):
    student = session.query(Student).filter(Student.name.like(f"%{nume_cautat}%")).all()
    
    if not student:
        print("Numele cautat nu a fost gasit.")
    
    for s in student:
        print(f"Studentul {s.name} a fost gasit.")
    
    
def main():
    
    create_db()
    
    while True:
        print("1. Adauga student")
        print("2. Afiseaza toti studentii")
        print("3. Actualizeaza student")
        print("4. Sterge student")
        print("5. Cautarea unui student")
        print("0. Exit")
        
        choice = int(input("Alege o optiune: "))
        
        if choice == 1:
            name = input("Nume: ")
            email = input("Email: ")
            
            add_student(name, email)
            
        elif choice == 2:
            list_students()
            
        elif choice == 3:
            student_id = int(input("Tastati id-ul studentului: "))
            
            name = input("Tastati noul nume: ")
            email = input("Tastati noul email: ")
            
            update_student(student_id, new_name=name if name else None, new_email=email if email else None)
            
        elif choice == 4:
            student_id = int(input("Tastati id-ul studentului: "))
            
            delete_student(student_id)
            
        elif choice == 5:
            nume_cautat = input("Tastati numele cautat: ")
            search_by_name(nume_cautat)
        
        elif choice == 0:
            print("Hai pa!")
            break

        else:
            print("Optiunea este invalida.")


if __name__ == '__main__':
    main()
