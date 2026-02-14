### Binary Search ###

# Algoritm:
# 1. Se iau 2 indici: "start" si "end"
# 2. Verificam daca "start" <= "end", conditie daca nu se intampla asta
# 3. Calculam mijlocul: "mid = (start + end) // 2"
# 4. Comparam elemntul din mijloc cu cheia, poate fi emag, mai mare sau mai mic
# 5. Repetam procesul pana gasim cheia sau pana se termina lista



# Pe baza algoritmului cautarii binare avem 2 varinate de implemetare
# Metoda 1 - Cautare binara iterativa
from typing import List


def binary_search_iter(lst: List[int], key: int) -> int:
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = int((start + (end - start)) / 2)
        if lst[mid] == key:   # Conditia 1 - elementul cautat este la mijloc
            return mid
        elif lst[mid] < key:  # Conditia 2 - elementul cautat este mai mare decat mijlocul
            start = mid + 1
        else:                 # Conditia 3 - elementul cautat este mai mic decat mijlocul
            end = mid -1

    return -1


# Lista sortata si elementul pe care vrem sa-l cautam
# test_list = [2, 3, 4, 10, 40]
# x = 3
# result_iter = binary_search_iter(test_list, x)
#
# if result_iter != -1:
#     print(f"Elementul {x} este prezent la indexul {result_iter}")
# else:
#     print(f"Elementul {x} nu este prezent in lista")

# Metoda 2 - Cautare binara recursiva
def binary_search_rec(lst: List[int], key: int, start: int = 0, end:int = None) -> int:
    # Initializam capul listei, daca nu e dat
    if end is None:
        end = len(lst) - 1

    # Conditia de oprire a recursivitatii
    # Daca elementul nu exista, ar trebui returnat ceva
    if start > end:
        return -1

    # Calculul mijlocului (similar cu exercitiul de mai sus)
    mid = start + (end - start) // 2

    # Cele 3 conditii (aici trebuie implementata recursivitatea in 2/3 cazuri
    if lst[mid] == key:
        return mid
    elif lst[mid] < key:
        return binary_search_rec(lst, key, mid + 1, end)
    else:
        return binary_search_rec(lst, key, start, mid - 1)


test_list = [2, 3, 4, 10, 40]
x = 10
result_rec = binary_search_rec(test_list, x)

if result_rec != -1:
    print(f"Elementul {x} este prezent la indexul {result_rec}")
else:
    print(f"Elementul {x} nu este prezent in lista")
