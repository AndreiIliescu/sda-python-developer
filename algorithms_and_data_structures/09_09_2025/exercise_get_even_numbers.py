### Get even numbers ###

# Numerele pare dintr-o lista.
# Input: Avem o lista de nr. intregi.
# Output: Vrem sa afisam doar numerele pare, iar la final sa aspunem cate nr. pare am gasit.

### Algoritm:
# 1. Start
# 2. Primeste o lista de numere intregi [numbers]
# 3. Creeaza o lista goala [even_numbers] pentru a stoca numerele pare
# 4. Pentru fircare numar "n" din lista [numbers]
## if n % 2 == 0 -> adauga "n" in [even_numbers].
# 5. Afiseaza lista [even_numbers]
# 6. Afiseaza si numarul de elemente din [even_numbers]
# 7. End

### Implementarea algoritmului in cod Python
from typing import List


def get_even_numbers(numbers: List[int]) -> List[int]:
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)

    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(f"Numerele pare sunt: {even_numbers}")
print(f"NUmarul de numere pare este: {len(even_numbers)}")
