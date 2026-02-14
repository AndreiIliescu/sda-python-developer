### Seturi (sets)
# Colecție neordonată de elemente unice.
# Exemplu 1:
s = {1, 2, 3, 2}
print(s)  # {1, 2, 3}


# Exemplu 2: operații cu seturi:
A = {1, 2, 3}
B = {3, 4}
print("Uniune:", A | B)
print("Intersectie:", A & B)
print("Diferența:", A - B)


# Exemplu 3:
s = {1, 2, 3}
s.add(4)       # adaugă element în set (dacă nu există deja)
s.remove(2)    # elimină elementul 2 din set
print("Set după add și remove:", s)
element = s.pop()  # elimină un element arbitrar din set
print(f"Element extras arbitrar din set: {element}, setul rămas:", s)
