### Încapsulare
# Ascunderea datelor prin convenție (prefix _ pentru protejat, __ pentru privat).
# Ex: accesul la variabilele interne de obicei se face prin metode.
class ExempluEncapsulare:
    def __init__(self):
        self._protejata = 1
        self.__privata = 2
    def afisare(self):
        print("Protejat:", self._protejata, "Privat:", self.__privata)

obj = ExempluEncapsulare()
obj.afisare()
# print(obj.__privata)  # Eroare: nu se poate accesa direct
