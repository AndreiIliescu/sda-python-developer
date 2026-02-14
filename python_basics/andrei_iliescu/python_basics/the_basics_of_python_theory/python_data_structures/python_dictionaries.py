### Dicționare (dictionaries)
# Colecție de perechi cheie:valoare, fără indici numerici.
# Exemplu de dicționar:
d = {"cheie1": 100, "cheie2": 200}
# Acces: d["cheie1"]
print(d["cheie1"])


# Exemplu 2: adăugare și iterare:
d["nou"] = 300
for cheie, valoare in d.items():
    print(f"{cheie} -> {valoare}")

# Exemplu 3: manipularea dicționarelor
dictionar = {'a': 1, 'b': 2}
dictionar['c'] = 3        # adaugă perechea 'c':3
print("Dicționar:", dictionar)
print("Elementele (cheie, valoare) din dicționar:", list(dictionar.items()))
valoare_b = dictionar.pop('b')  # elimină și returnează valoarea pentru cheia 'b'
print("Valoarea eliminată pentru 'b':", valoare_b)
print("Dicționar după pop('b'):", dictionar)
