### Scope-ul variabilelor
# Variabile globale: definite în afara oricărei funcții (accesibile peste tot în modul).
# Variabile locale: definite în interiorul unei funcții (există doar acolo).
# Exemplu ilustrativ:
x = 100  # globală
def modifica():
    x = 50  # locală (față de funcție)
    print(f"În funcție x = {x}")
modifica()
print(f"În afara funcției x = {x}")

# variable scope
# Scope-ul variabilelor - local vs global vs nonlocal:contentReference[oaicite:10]{index=10}.
# Variabilele locale declarate într-o funcție sunt accesibile doar în interiorul ei. Variabilele globale, declarate în exteriorul oricărei funcții, pot fi accesate oriunde:contentReference[oaicite:11]{index=11}.
# Keyword-ul `global` este folosit în interiorul unei funcții pentru a specifica că lucrăm cu variabila globală, permițându-i să fie modificată:contentReference[oaicite:12]{index=12}.
# (Există și `nonlocal` pentru variabile din funcții exterioare într-un context închis.)

x = 5  # variabilă globală
def modifica_fara_global():
    x = 10  # variabilă locală cu același nume
    print("În funcție (fără global), x =", x)

modifica_fara_global()
print("În afara funcției, x =", x)  # rămâne 5, deoarece nu am folosit global

y = 5
def modifica_cu_global():
    global y
    y = 15  # modifică variabila globală y
    print("În funcție (cu global), y =", y)

modifica_cu_global()
print("În afara funcției, y =", y)  # acum este 15

# Exemplu nonlocal:
def exterior():
    message = "Salut"
    def interior():
        nonlocal message
        message = "Bună ziua"
    interior()
    print("Mesaj interior modificat:", message)

exterior()
