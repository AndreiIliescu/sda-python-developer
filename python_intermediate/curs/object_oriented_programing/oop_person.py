### Inheritance (Mostenire) ###
from tkinter.messagebox import showerror


# Clasa de baza: Parent (Parinte)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def who_am_i(self):
        print(f"Salut! Eu sunt {self.name} si am {self.age} de ani.")

    def __str__(self):
        # type(self) - ne va returna tipul obiectului care apeleaza functia
        # __name__ - este un string cu numele clasei
        return f"{self.name} are {self.age} de ani - {type(self).__name__}"


# Clasa copil (Child)
# Clasa Employee "mosteneste" toate proprietatile clasei Person
class Employee(Person):
    def __init__(self, name, age, rate, working_hours):
        Person.__init__(self, name, age)
        self.rate = rate
        self.working_hours = working_hours

    def show_finance(self):
        return self.rate * self.working_hours

    def who_am_i(self):
        # In acest caz apelam metoda originala
        # Person.who_am_i(self)
        # sau folosim cuvantul "super()" care face referire la clasa de baza
        super().who_am_i()

        # Dupa care completam functia cu cod in plus
        print(f"Si fac {self.show_finance()}")


class Student(Person):
    def __init__(self, name, age, scholarship):
        Person.__init__(self, name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


# Mostenire-multipla (Multiple Inheritance)
class WorkingStudent(Employee, Student):
    def __init__(self, name, age, rate, working_hours, scholarship):
        Employee.__init__(self, name, age, rate, working_hours)
        Student.__init__(self, name, age, scholarship)

    # Override (Suprascrierea) unei functii
    # Redefinim functia din clasa de baza cu exact aceeasi parametri si return type
    # Codul din noua functie il va inlocui pe cel vechi
    def show_finance(self):
        return self.rate * self.working_hours + self.scholarship


p1 = Person("Andrei", 24)
print(p1)
print(p1.who_am_i())

print()

p2 = Person("Mina", 20)
print(p2)
print(p2.who_am_i())

print()

e1 = Employee("Marius", 35, 160, 8)
print(e1)
print(e1.show_finance())
print(e1.who_am_i())

print()

s1 = Student("Andreea", 25, 1000)
print(s1)
print(s1.show_finance())

print()

ws1 = WorkingStudent("Beatrice", 27, 25, 4, 500)
print(ws1)
print(ws1.show_finance())
print(ws1.who_am_i())

print("\n\n\n")

### Polymorphism - functionalitate comuna intre mai mulye obiecte ###
def check_finance(obj):
    # Varianta directa care poate da eroare daca obj nu este tip bun de date
    # print(f"Finatele sunt: {obj.show_finance()}")

    # Optional putem scrie un try/except pt. a prinde o posibila AttributeError
    try:
        print(f"Finatele sunt: {obj.show_finance()}")
    except AttributeError:
        print("Obj nu are functia 'show_finance()'")


check_finance(e1)
check_finance(s1)
check_finance(ws1)
check_finance(10) # -> Eroare! int nu are functia "show_finance()"
