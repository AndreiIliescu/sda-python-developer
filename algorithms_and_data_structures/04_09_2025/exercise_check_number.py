### Check number ###

# Cerinta: Verificam daca un numar este pozitiv, negativ, sau zero.

# Algoritm pas cu pas:
# 1. Start
# 2. Scriem (de la tastatura) un numar si-l stocam in variabila "number"
# 3. Verificam conditii:
## if num == 0 -> returnam "num este egal cu zero";
## elif num > 0 -> returnam f"{num} este pozitiv";
## else num < 0 -> returnam f"{num} este negativ".
# 4. Stop

# O functie "check_number" care verifica daca un nr. este par sau nu.
# Functia primeste ca input un "int" si verifica sa returneze un "str".

number = int(input("Introdu un numar: "))

def check_number(num: int) -> str:
    if num == 0:
        result = "num este egal cu zero"
    elif num > 0:
        result = f"{num} este pozitiv"
    else:
        result = f"{num} este negativ"
    return result


print(check_number(number))
