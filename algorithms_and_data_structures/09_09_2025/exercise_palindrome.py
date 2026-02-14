### Palindrome ###

# Cerinta: Scrie o functie care primeste o lista de cuvinte si returneaza doar cuvintele care sunt palindrom.
# Palindrom = se citesc la fel si de la stanga si de la dreapta.
# ex.: "level", "radar", "Ana".

# Algoritm:
# 1. Start
# 2. Primeste lista de cuvinte [list_of_words]
# 3. Creaza o lista goala [result]
# 4. Facem un for pentru parcurgere fiecare cuvant (w) din [list_of_words]
# 5. Verificam daca "w" este egal cu "w" inversat (w[::-1])
# 6. Daca se respecta -> w este adagat in lista
# 7. Return lista [result]
# 8. End

### Implementarea algoritmului in cod Python
from typing import List


def palindrom(list_of_words: List[str]) -> List[str]:
    result = []

    for w in list_of_words:
        if w == w[::-1]:
            result.append(w)

    return result


print(palindrom(["bob", "ana", "cat", "level", "python", "radar", "tea"]))
