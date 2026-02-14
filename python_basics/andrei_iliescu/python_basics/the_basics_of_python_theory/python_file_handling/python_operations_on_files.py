# Operatii de citire și scriere în fișiere:
# open(), read(), readline(), readlines(), write(), close(), și context manager.
# Exemplu 1: citire din fișier text:
with open('exemplu.txt', 'w') as f:
    f.write("Linia 1\nLinia 2\n")
with open('exemplu.txt', 'r') as f:
    continut = f.read()
    print("Conținut fișier:\n", continut)


# Exemplu 2: citire linie cu linie și scriere filtrată:
with open('exemplu.txt', 'r') as f_in, open('filtrate.txt', 'w') as f_out:
    for linie in f_in:
        if "1" in linie:
            f_out.write(linie.upper())
# Acest cod creează un nou fișier cu liniile care conțin "1", convertite la majuscule.
