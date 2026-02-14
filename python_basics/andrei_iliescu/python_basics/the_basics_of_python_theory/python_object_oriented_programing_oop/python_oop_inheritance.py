### Moștenire
# O clasă derivată poate extinde o clasă de bază (superclass).
# Exemplu:
class Animal:
    def vorbeste(self):
        print("Sunet generic")

class Caine(Animal):
    def vorbeste(self):
        print("Ham ham!")

anim = Animal()
dog = Caine()
anim.vorbeste()  # Sunet generic
dog.vorbeste()   # Ham ham!


# Moștenire cu apel la super:
class Om:
    def __init__(self, nume):
        self.nume = nume

class Programator(Om):
    def __init__(self, nume, limbaj):
        super().__init__(nume)
        self.limbaj = limbaj

p = Programator("Alice", "Python")
print(p.nume, "folosește", p.limbaj)
