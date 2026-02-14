### Weird string ###

# Cerinta: Scrie o functie to_weird_case, care primeste un sir de caractere si il returneaza astfel:
## toate literele de pe pozitii pare (indexand de la zero) sa fie UPPERCASE;
## toate literele de pe pozitii impare sa fie lowercase.

## ex.: "String" -> "StRiNg"
## ex.: "Algorithms and data structures" -> AlGoRiThMs AnD DaTa StRuCtUrE

### Algoritm:
# 1. Start
# 2. Initializam "i = 0", pentru a urmari pozitia fiecarui caracter in cadrul fiecarui cuvant
# 3. "new_string" = "" -> aici construim rezultatul
# 4. Parcurgem fiecare caracter
# 5. Verificam daca un caracter este un "spatiu"
# 6.Continuam pana terminam sirul
# 7. Returnam rezultatul
# 8. End

### Implementarea algoritmului in cod Python

def to_weird_case(string: str) -> str:

    i = 0
    new_string = ""

    for character in string:
        if character != " ":
            if i % 2 == 0:
                new_string += character.upper() # litere de pe pozitii pare -> UPPERCASE.
            else:
                new_string += character.lower() # literele de pe pozitii impare -> lowercase.

            i += 1 # trecem la urmatorul caracter

        else:
            i = 0 # la "spatii" -> resetam indexul pt. un cuvant nou.
            new_string += character # pastram spatiul in rezultat (in noul string).

    return new_string


print(to_weird_case("Algorithms and data structures"))
