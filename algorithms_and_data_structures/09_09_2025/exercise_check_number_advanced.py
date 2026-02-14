### Check number advanced ###

# Cerinta: Veriicare unui numar daca este pozitiv/negativ, par/impar si multiplu de cinci.
# Input: O variabila de tip "int".
# Output: Un mesaj de genul "Numar pozitiv, par, multiplu de cinci.

### Algoritm:
# 1. Start
# 2. Primeste un numar (de la user) de tip "int"
# 3. Verificam daca nr. este pozitiv negativ sau zero
## if num > 0: -> mesaj = "Numarul este pozitiv";
## elif num < 0: -> mesaj = "Numarul este negativ";
## else: -> mesaj = "Numarul este zero".
# 4. Verificam paritatea (numar par sau impar);
## if num != 0 ("!=" inseamna diferit de);
## if num % 2 == 0: -> mesaj += " si par";
## else -> mesaj += " si imapr".
# 5. Verificam daca este multiplu de cinci
## if num != 0;
## if num % 5 == 0: -> mesaj += " si multiplu de cinci";
# 6. Returnare mesaj
# 7. End

### Implementarea algoritmului in cod Python
def check_number_advanced(num: int) -> str:
    if num > 0:
        mesaj = "Numarul este pozitiv"
    elif num < 0:
        mesaj = "Numarul este negativ"
    else:
        mesaj = "Numarul este zero"

    if num != 0:
        if num % 2 == 0:
            mesaj += " si par"
        else:
            mesaj += " si impar"

    if num != 0 and num % 5 == 0:
        mesaj += " si multiplu de cinci."
    else:
        mesaj += " si nu este multiplu de cinci."

    return mesaj


n = int(input("Introdu un numar: "))
rezultat = check_number_advanced(n)
print(rezultat)
