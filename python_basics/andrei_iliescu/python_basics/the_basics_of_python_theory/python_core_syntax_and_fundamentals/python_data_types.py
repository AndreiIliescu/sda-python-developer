### Tipuri de date (data types)
# Tipurile de date de bază în Python includ:
# - int (număr întreg), float (număr zecimal), complex (număr complex),
# - str (șir de caractere), bool (True/False), NoneType (None).
# Python este dinamic tipizat, deci tipul variabilei este inferat la asignare.
# Exemplu:
a: int = 5
b: float = 3.14
c: complex = 2 + 3j
d: str = "Salut"
e: bool = True
f = None  # NoneType
print(type(a), type(b), type(c), type(d), type(e), type(f))


# Exemple de tipuri și utilizări:
print(int("10") + 5)       # Convertește șirul "10" la int și adună -> 15
print(float(2) / 3)        # Împărțire cu conversie la float -> ~0.6667
print(str(123) + "45")     # "12345" concatenat
print(bool(0), bool(42))   # False True (0 este considerat fals, iar orice alt număr nenul adevărat)
