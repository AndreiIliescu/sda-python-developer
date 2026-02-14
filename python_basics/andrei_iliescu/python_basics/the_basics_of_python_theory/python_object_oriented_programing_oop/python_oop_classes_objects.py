### Clase și obiecte
# Clasa este un tip definit de utilizator; obiectul este o instanță a clasei.
# Exemplu 1 de clasă și obiect:
class Pisica:
    def __init__(self, nume):
        self.nume = nume
    def miaumiau(self):
        print(f"{self.nume} spune 'Miau!'")

pisic = Pisica("Tom")
pisic.miaumiau()


# Exemplu 2: clasă cu mai multe metode și atribute:
class Dreptunghi:
    def __init__(self, latime, lungime):
        self.latime = latime
        self.lungime = lungime
    def aria(self):
        return self.latime * self.lungime
    def perimetru(self):
        return 2*(self.latime + self.lungime)

drept = Dreptunghi(3, 4)
print("Aria:", drept.aria(), "Perimetrul:", drept.perimetru())
