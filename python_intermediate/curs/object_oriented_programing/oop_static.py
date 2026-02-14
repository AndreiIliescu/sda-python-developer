### Inheritance (Mostenire) ###

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

    # Metoda statica
    @staticmethod
    def is_name_correct(name):
        if name[0].isupper() and len(name) > 3:
            return True

        return False

    # Metoda de clasa (classmethode)
    @classmethod
    def create_from_string(cls, text):
        name, age, scholarship = text.split()
        age, scholarship = int(age), int(scholarship)
        # Cuvantul "cls" este completat automat de Python cu numele clasei in care suntem.
        # In aces caz "cls" este echivalent cu a scrie Student.
        if cls.is_name_correct(name):
            return cls(name, age, scholarship)
        return None


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


# Exemple functii statice/classmethods
# Functiile statice/class se folosesc:
## NumeClasa.nume_functie()
print(Student.is_name_correct("Todd")) # -> returns True
print(Student.is_name_correct("AI")) # -> returns False

# s1 = Student("Andreea", 25, 1000)
s1 = Student.create_from_string("Andreea 25 1000")
