## Control flow
### break, continue și pass
# Instrucțiuni care modifică fluxul buclelor:
# - break: oprește imediat bucla curentă și iese din ea.
# - continue: sare peste restul corpului buclei și trece la următoarea iterație.
# - pass: nu face nimic (este un „place holder” când nu vrem nicio acțiune).
# Exemplu 1 de utilizare break/continue într-o buclă while:
n = 0
while n < 5:
    n += 1  # incrementare n la fiecare iterație
    if n == 4:
        break   # iese din buclă când n ajunge 4
    if n == 2:
        continue  # sare restul instrucțiunilor și continuă de sus
    print(f"Valoare n: {n}")
# Rezultat: Valoare n: 1,  Valoare n: 3


# Exemplu 2: căutarea unui element în listă folosind break și continue
numbers = [3, 7, 1, 9, 5, 7, 8]
target = 7
found = False
for num in numbers:
    if num < 0:
        continue  # ignorăm numerele negative (deși nu sunt aici)
    if num == target:
        print(f"Element {target} găsit!")
        found = True
        break
if not found:
    print("Elementul nu a fost găsit în listă.")
