### Input și Output
# input() citește de la tastatură (returnează șir).
nume = input("Cum te cheamă? ")
print(f"Salut, {nume}!")  # print() afișează text la ecran.

# Funcții built-in esențiale:
# - print(): afișează valori în consolă.
# - len(obj): returnează lungimea obiectului iterabil (număr elemente).
# - range(n): generează secvență de la 0 la n-1 (utile în bucle).
# - max(seq)/min(seq): returnează valoarea maximă/minimă din secvență.
# - str.upper()/str.lower(): convertesc șirul la majuscule/minuscule:contentReference[oaicite:17]{index=17}:contentReference[oaicite:18]{index=18}.
# - str.title(): capitalizează primul caracter al fiecărui cuvânt din șir:contentReference[oaicite:19]{index=19}.
# - dict.items(): întoarce o listă (view) de perechi (cheie, valoare):contentReference[oaicite:20]{index=20}.

# Exemplu 1: print, len, range, max, min
cuvinte = ["mere", "pere", "banane"]
print("Lista cuvintelor:", cuvinte)
print("Număr de cuvinte:", len(cuvinte))
print("Max alfabetically:", max(cuvinte))
print("Min alfabetically:", min(cuvinte))
for i in range(len(cuvinte)):
    print(f"Cuvântul {i} este {cuvinte[i]}")

# Exemplu 2: metode pe șiruri și items pe dicționar
text = "Hello World"
print(text.upper(), "-", text.lower(), "-", text.title())
persoana = {"nume": "Ana", "vârstă": 25}
for k, v in persoana.items():
    print(k, ":", v)
