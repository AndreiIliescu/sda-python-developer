### Anagrame ###

# Cerinta: SCrie o functie care gaseste toate anagramele unui cuvant din lista furnizata.
# Input: O lista de string-uri.
# Output: O lista de string-uti -> Cuvintee gasite trebuie returnate sub forma de lista.

# Anagramele sunt doua cuvinte care contin exact aceleasi litere.
# ex.: "listen" & "silent" == True.
# ex.: "cat" & "tap" == False.
# ex.: "night" & "thing" == True.

### Algoritm:
# 1. Start
# 2. Definim functia + argumentele functie + ce tip de date returneaza
# 3. Sortare a literelor
# 4. Creare lista goala (pe care o populam ulterior)
# 5. For in lista de cuvinte, si daca doua cuvinte sunt contin aceleasi liste, le adaugam in lista goala
# 6. Functia returneaza lista populata cu anagrame
# 7. End

### Implementarea algoritmului in cod Python
from typing import List


def anagrams(word: str, list_of_words: List[str]) -> List[str]:
    sorted_word = sorted(word)
    result = []
    for w in list_of_words:
        if sorted(w) == sorted_word:
            result.append(w)
    return result


print(anagrams("abba", ["aabb", "abcd", "bbaa", "dada"]))
