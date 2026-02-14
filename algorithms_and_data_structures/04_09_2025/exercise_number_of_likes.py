### Number of likes ###

# Cerinta ex. 1: Implementeaza sistemul de afisare a numarului de like-uri asa cum se intampla pe Facebook.

# Structura flowchart-ului ar fi:

# 1. Start
# 2. Citeste lista de "names"
# 3. Obtinem "number_of_names = len(names)", adica lungimea listei
# 4. Verificare conditii:
## if number_of_names == 0 -> afiseaza 'print("Nimeni nu a dat like")';
## if number_of_names == 1 -> afiseaza 'print(f"{names[0]} a dat like!")';
## if number_of_names == 2 -> afiseaza 'print(f"{names[0]} si {names[1]} au dat like!")';
## if number_of_names == 3 -> afiseaza 'print(f"{names[0]}, {names[1]} si {names[2]} au dat like!")';
## else (numbers_of_names > 3) -> afiseaza 'print(f"{names[0]}, {names[1]} si {number_of_names - 2} au dat like!")'.
# 5. End

from typing import List
# typing = un modul built-in ce iti permite sa spui ce tip de date se accepta la parametri sau ce tip retuneaza functia.
# List = un tip generic pentru liste.


def likes(names: List[str]) -> str: # Functia are ca parametru o lista de str si va returna un string.
    number_of_names = len(names)

    if number_of_names == 0:
        format_output = "Nimeni nu a dat like."
    elif number_of_names == 1:
        format_output = f"{names[0]} a dat like!"
    elif number_of_names == 2:
        format_output = f"{names[0]} si {names[1]} au dat like!"
    elif number_of_names == 3:
        format_output = f"{names[0]}, {names[1]} si {names[2]} au dat like!"
    else:
        format_output = f"{names[0]}, {names[1]} si alte {number_of_names - 2} persoane au dat like!"

    return format_output


# In final algoritmul ar trebuie sa functioneze astfel:
print(likes([]))  ## => "nobody likes it"
print(likes(["Peter"]))  ## => "Peter likes it!"
print(likes(["Peter", "Anna"]))  ## => "Peter and Anna like it"
print(likes(["Peter", "Anna", "Mark"]))  ## => "Peter, Anna and Mark like it"
print(likes(["Peter", "Anna", "Mark", "Ola"]))  ## => "Peter, Anna and 2 other people like it"


# Reprezentarea binara a unor numere folosind functia built-in "bin()".
print(bin(5))
print(bin(10))
print(bin(4567))
