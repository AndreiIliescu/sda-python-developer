### Polimorfism
# Clase diferite pot avea metode cu același nume, comportament diferit.
# Exemplu:
class A:
    def afis(self):
        print("Clasa A")
class B:
    def afis(self):
        print("Clasa B")

lista = [A(), B()]
for obj in lista:
    obj.afis()  # Deoarece ambele au metoda afișată, se apelează corespunzător
