""" Pattern-ul 'Adapter' poate fi implememtat in 2 moduri:
1. orientat pe obiecte - unde obiectul 'Adapter' agrega obiectul adoptat (are o referinta catre el)
2. orientat pe clasa - unde adaptorul mosteneste atat interfata tinta, cat si clasa obiectului adoptat

Implementare 1 - mod orientat pe obiect
Interfata tinta cu care vrem sa lucram """
class Student:
    def get_full_name(self):
        pass                                   # Metoda ce va returna numele complet al studentului


    def get_contact_details(self):
        pass


    def is_adult(self):
        pass


    def get_results(self):
        pass                                   # Metoda care va returna notele studentului


# Clasa care nu este compatibila cu "Student"
class Favorite:
    def __init__(self, first_name, last_name, email, age, grades):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._age = age
        self._grades = grades                  # Lista cu notele studentului


    def get_first_name(self):
        return self._first_name


    def get_last_name(self):
        return self._last_name


    def get_email(self):
        return self._email


    def get_age(self):
        return self._age


    def get_grades(self):
        return self._grades


# Adaptor care transmite "Favourite" intr-un "Student"
class FavoriteAdapter(Student):
    def __init__(self, Favorite):
        self._Favorite = Favorite             # Obiectul "Favorite" care trebuie adaptat


    def get_full_name(self):
        return self._Favorite.get_first_name() + " " + self._Favorite.get_last_name()


    def get_contact_details(self):
        return self._Favorite.get_email()


    def is_adult(self):
        return self._Favorite.get_age() >= 18


    def get_results(self):
        return self._Favorite.get_grades()


def main():
    students = [FavoriteAdapter(Favorite('Steven', 'Morgan', 'sm@gmail.com', 19, [3, 4, 5])),
                FavoriteAdapter(Favorite('Maria', 'Smith', 'mk@hotmail.com', 17, [4, 5, 4])),
                FavoriteAdapter(Favorite('Joanna', 'Noris', 'jn@yahoo.com', 21, [2, 4, 6]))]

    for s in students:
        print(
            f"{'Adult' if s.is_adult() else 'Child'} {s.get_full_name()} [{s.get_contact_details()}]: {s.get_results()}")


if __name__ == '__main__':
    main()

print()

""" Implementare 2 - mod orientat pe clasa """
class Student:
    def get_full_name(self):
        pass


    def get_contact_details(self):
        pass


    def is_adult(self):
        pass


    def get_results(self):
        pass


""" Adaptorul care mosteneste atat 'Favourite' cat si 'Student' """
class Favorite:
    def __init__(self, first_name, last_name, email, age, grades):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._age = age
        self._grades = grades


    def get_first_name(self):
        return self._first_name


    def get_last_name(self):
        return self._last_name


    def get_email(self):
        return self._email


    def get_age(self):
        return self._age


    def get_grades(self):
        return self._grades


class FavoriteAdapter(Student, Favorite):
    # Constructor: Initializare clasa de baza "Favourite" cu datele studentului
    def __init__(self, first_name, last_name, email, age, grades):
        super().__init__(first_name, last_name, email, age, grades)


    # get_full_name
    def get_full_name(self):
        return self.get_first_name() + " " + self.get_last_name()


    # get_contact_details
    def get_contact_details(self):
        return self.get_email()


    # is_adult
    def is_adult(self):
        return self.get_age() >= 18


    # get_result
    def get_results(self):
        return self.get_grades()


def main():
    students = [FavoriteAdapter('Steven', 'Morgan', 'sm@gmail.com', 19, [3, 4, 5]),
                FavoriteAdapter('Maria', 'Smith', 'mk@hotmail.com', 17, [4, 5, 4]),
                FavoriteAdapter('Joanna', 'Noris', 'jn@yahoo.com', 21, [2, 4, 6])]

    for s in students:
        print(
            f"{'Adult' if s.is_adult() else 'Child'} {s.get_full_name()} [{s.get_contact_details()}]: {s.get_results()}")


if __name__ == '__main__':
    main()
