### Funcții cu argumente
# Parametrii permit transmiterea de date în funcție.
# Exemplu:
def inmultire(x, y):
    prod = x * y
    print(f"{x} * {y} = {prod}")

inmultire(5, 6)

# args / kwargs
# Funcții - parametrii *args și **kwargs permit funcțiilor să primească un număr variabil de argumente
# poziționale și respectiv cuvânt-cheie:contentReference[oaicite:7]{index=7}.
# *args (argumente variabile) sunt colectate ca un tuplu în interiorul funcției:contentReference[oaicite:8]{index=8}.
# **kwargs (keyword arguments) sunt colectate ca un dicționar de perechi cheie=valoare:contentReference[oaicite:9]{index=9}.

# Exemplu 3: funcție cu *args
def aduna(*args):
    total = 0
    for num in args:
        total += num
    return total

print(aduna(1, 2, 3))     # 6
print(aduna(10, 20, 30, 40))  # 100

# Exemplu 4: funcție cu **kwargs
def afiseaza(**kwargs):
    for cheie, valoare in kwargs.items():
        print(f"{cheie} = {valoare}")

afiseaza(nume="Alice", varsta=30, oras="București")
