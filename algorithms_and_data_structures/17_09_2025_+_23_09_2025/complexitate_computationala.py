'''Completitatea computationala = spune cat de greu este pentru calculator sa rezolve o problema cand datele devin din
ce in ce mai mari

Complexitatile sunt de mai multe feluri:
1. Complexitate constanta
2. Complexitate logaritmica
3. Complexitate liniara
4. Complexitate liniar-logaritmica
5. Complexitate polinomiala
6. Complexitate exponentiala
7. Complexitate factoriala'''

# / ================================================================================================================== /

'''Cazul 1 - Complexitate constanta: O(1)'''
numbers  = [10, 20, 30, 40]
first = numbers[0] # returneaza primul element -> constant
print(first)

sum_two = 5 + 7 # adunarea a doua numere -> constant
new_var = 100 # creara variabila nou -> constant

print()

# / ================================================================================================================== /

'''ConnectionErrorCazul 2 - Complexitate logaritmica: O(log n)
- timpul sau memoria cresc logaritmic in functie de datele de intrare
- timpul de executie creste foarte incet, chiar daca lista devine foarte mare'''

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 7))
'''- pasul 1 -> raman n/2 elem.
- pasul 2 -> raman n/4 elem.
- pasul 3 -> raman n/8 elem.
- ... pana ramane 1 elem.
- practic, numarul de pasi ar fi log2(n) -> logaritm in baza 2 din n'''
print()

# / ================================================================================================================== /

'''Cazul 3 - Complexitate liniara: O(n)
- timpul si/sau memoria cresc proprotional cu dimensiunea datelor de intrare'''

# iterarea prin toate elementele unei liste sau calcularea sumei lor
numbers_2 = [1, 2, 3, 4, 5]
total = 0
for num in numbers_2:
    total += num
print(total)

print()

# / ================================================================================================================== /

'''Cazul 4 - Complexitate liniar-logaritmica: O(n * log n)
- sortarile (functiile "sorted()") in Python sunt O(n * log n)
- algoritmul QuickSort, MergeSort, HeapSort'''

# ===================================================| QuickSort |======================================================

'''ex.: QuickSort
Pasii algoritmului:
4.1. Alegem un pivot (luam primul element ca pivot)
- Pivotul este 5
- Impartim lista in 2 subliste
- left = [3, 4, 2] (toate sunt <= 5)
- right = [8] (toate care sunt > 5)

4.2. Luam lista "left": [3, 4, 2] (luata de la punctul 1.)
- Pivot = 3
- left = [2] (toate <= 3)
- right = [4] (toate > 3)
- left sortat = [2, 3, 4]

4.3. Luam lista "right": [8] (luata de la punctul 1.)
- Lista are un element -> deja sortata: [8]

4.4. Combina toate
- [left sortat] + pivot + [right sortat]
- [2, 3, 4] + [5] + [8]
- [2, 3, 4, 5, 8]

Implementarea algoritmului QuickSort:'''
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quicksort(left) + [pivot] + quicksort(right)


arr = [5, 3, 8, 4, 2]
print(quicksort(arr))
print()

'''QuickSort - pentru sortare rapida in memorie foarte eficient (in Python functiile "sorted()" si "sort()" folosesc Timsort)'''

# ===================================================| MergeSort |======================================================

'''ex.: MergeSort
# Pasii algoritmului:
# MergeSort - algoritm divide et impera, impartirea se combinarea se fac diferit fata de QuickSort
# Pasul 1: [5, 3, 8, 4, 2] -> impartim lista in 2 jumatati aprox. egale
## [5, 3, 8, 4, 2] -> [5, 3] si [8, 4, 2]

# Pasul 2: Sorteaza recursiv fiecare jumatate (aplicand MergeSort)
## [5, 3] -> impartim in [5] si [3] -> combinam -> [3, 5]
## [8, 4, 2] -> impartim in [8] si [4, 2] -> [4, 2] -> in [2, 4] -> combinam cu [8] -> [2, 4, 8]

# Pasul 3: Combinam cele 2 jumatati
## [3, 5] + [2, 4, 8] -> [ 2, 3, 4, 5, 8]

# Implementarea algoritmului MergeSort:'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0 # indexi pt. a parcurge sublistele "left" si "right"

    while i < len(left) and j < len(right): # cat timp nu am ajuns la finalul niciunei subliste
        if left[i] < right[j]:              # comparam elementele curente din ambele subliste
            result.append(left[i])          # adaugam elementul mai mic din "left" in "result"
            i += 1
        else:
            result.append(right[i])         # adaugam elementul mai mic din "right" in "result"
            j += 1

        result += left[i:] # adaugam la rezultat orice element neprocesat
        result += right[j:]

    return result

'''MergeSort - pentru sortari cu multiple criterii si unde stabilitatea e importanta'''

# / ================================================================================================================== /

'''Cazul 5 - Complexitate polinomiala: O(n^c)
- timpul si meomoria cresc proportional cu patratul, cubul, etc.
- Bubble Sort, Insertion Sort, Selection Sort, bucla in bucla (for in for)
- algoritmi pentru grafuri cu matrice de adiacenta: parcurgerea tuturor perechilor de noduri'''

# ===================================================| BubleSort |======================================================

'''Pasul 1: prima iteratie (i = 0)
- Comparam elementele vecine si il ducem pe cel mai mare la finalul listei:
* compare 5 & 3 -> 5 > 3 -> swap -> [3, 5, 8, 4, 2]
* compare 5 & 8 -> 5 < 8 -> nu schimbam -> [3, 5, 8, 4, 2]
* compare 8 & 4 -> 8 > 4 -> swap -> [3, 5, 4, 8, 2]
* compare 8 & 2 -> 8 > 2 -> swap -> [3, 5, 4, 2, 8]
- Cel mai mare element (8) a ajuns ka final

suntem aici: [3, 5, 4, 2, 8]
Pasul 2: a doua iteratie (i = 1)
- Ignoram ultimul element (8) pt. ca este deja la locul lui
* compare 3 & 5 -> 3 < 5 -> nu schimbam -> [3, 5, 4, 2, 8]
* compare 5 & 4 -> 5 > 4 -> swap -> [3, 4, 5, 2, 8]
* compare 5 & 2 -> 5 > 2 -> swap -> [3, 4, 2, 5, 8]
- Al doilea cel mai mare element (5) e acum pe pozitia corecta

suntem aici: [3, 4, 2, 5, 8]
Pasul 3: a treia iteratie (i = 2)
* compare 3 & 4 -> 3 < 4 -> nu schimbam -> [3, 4, 2, 5, 8]
* compare 4 & 2 -> 4 > 2 -> swap -> [3, 2, 4, 5, 8]
- Al treilea cel mai mare element (4) este la locul lui

suntem aici: [3, 2, 4, 5, 8]
Pasul 4: a patra iteratie (i = 3)
* compare 3 & 2 -> 3 > 2 -> swap -> [2, 3, 4, 5, 8]
- Toate elementele sunt acum sortate'''

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False  # Initial nu s-a facut niciun swap
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # interschimbam elementele (swap)
                swapped = True

        if not swapped:
            # Daca nu s-a facut niciun swap, lista e deja sortata
            break

    return arr


arr_2 = [5, 3, 8, 4, 2]
print(bubble_sort(arr_2))
print()
arr_3 = [1, 2, 3, 4, 5]
print(bubble_sort(arr_3))
print()

'''Swap in Python
a = 5
b = 3
a, b = b, a

arr = [5, 3, 8, 4, 2]
arr[0], arr[1] = arr[1], arr[0]
print(arr)'''

# / ================================================================================================================== /

'''Cazul 6 - Complexitate exponentiala: O(c^n)
- algoritmii acestia nu sunt foarte eficienti si de obicei se evita implementarea lor
- Fibonacci recursiv'''

def fib_recursive(n):
    if n <= 1:
        return n

    return fib_recursive(n - 1) + fib_recursive(n - 2)


print(fib_recursive(15)) # Aici ne va afisa al 15 lea element din sirul Fibonacci
print()

# / ================================================================================================================== /

'''Cazul 7 - Complexitate factoriala: O(n!)
- cel mai rau scenariu: chiar si o crestere mica a datelor face algoritmul impracticabil
- determinarea permutarilor (se foloseste: "from itertools import permutations") - pentru a genera permutarile'''

def permut(arr):
    if len(arr) == 0:
        return [[]]

    result = []

    for i in range(len(arr)):
        rest = arr[:i] + arr[i + 1:] # Construim lista fara elementul curent (doar cu restul elementelor)

        for p in permut(rest):
            result.append([arr[i]] + p) # Adaugam elementul curent la inceputul fiecarei permutari

    return result


arr_4 = [1, 2, 3]
# Lista de permutari: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(permut(arr_4))
print()

'''Varianta automata (mai simpla pentru permutari, folosind functia built-in "permutations" din modulul "itertools"'''
from itertools import permutations


perm = list(permutations(arr_4)) # "permutations()" returneaza un iterator de tuple, nu liste
print(perm)
print()

perm_as_list = [list(p) for p in perm]
print(perm_as_list)

# / ================================================================================================================== /

'''Lucru individual:
- Pentru fiecare tip de complexitate, sa creati un exemplu propriu de cod, care sa ilustreze acel tip de complexitate
* exemplul trebuie sa functioneze in Python
* explicati intr-o propozitie de ce complexitatea exemplului respectiv corespunde tipului respectiv.'''
