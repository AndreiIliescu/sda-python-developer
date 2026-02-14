# ==========================================| Complexitate constanta - O(1) |===========================================

d = {"a": 1, "b": 2}
print(d["a"])
print()

'''Codul de mai sus acceseaza constant valoarea primei chei din dictionar'''

# =====================================| Complexitate logaritmica - O(log n) |==========================================

import math


n = 1024
print(math.log2(n))
print()

'''Utilizarea functiei "log2" scade la jumatate cu fiecare pas problema'''

# ========================================| Complexitate liniara - O(n) |===============================================

max_value = max([4, 2, 9, 1])
print(max_value)
print()

'''Acest cod cauta de fiecare data elementul maxim din lista data'''

# ================================| Complexitate liniar-logaritmica - O(n * log n) |====================================

arr = [6, 2, 9, 1]
arr.sort()
print(arr)
print()

'''Functia "sort()" aranjeaza in ordine crescatoare elementele listei'''

# ======================================| Complexitate polinomiala - O(n^c) |===========================================

for i in range(5):
    for j in range(5):
        print(i, j)
print()

'''Exemplu de bucle imbricate (for in for)'''

# =====================================| Complexitate exponentiala - O(c^n) |===========================================

def power_set_size(n):
    return 2 ** n


print(power_set_size(6))
print()

'''Numărul de submulțimi crește exponențial.'''

# ========================================| Complexitate factoriala - O(n!) |===========================================

from itertools import permutations


print(list(permutations([1, 2, 3])))

'''Am folosit "from itertools import permutations" - pentru a genera permutarile'''
