# Aplicatiile functiilor lambda
# map, filter, reduce

# map() function
numbers = [1, 2, 3, 4, 5]
# Varianta 1 - (Codul clasic pentru a crea o lista cu elemente dublate)
# doubled = []
# for x in numbers:
#   doubled.append(x * 2)

# Varianta 2 - (Cu lambda)
# Functia "map()" ia ca parametrii o functie lambda care descrie operatiunea aplicata pe elementele din lista
# si lista pe care se va aplica operatiunea
# "map()" returneaza o lista noua
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Functiile lambda sunt foarte rapide
# from curs.exercitii_de_la_curs.class_exercise_cm_timer import TimeIt


# numbers = range(50000000)
# with TimeIt():
#     print("Time for lambda")
#     doubled = map(lambda x: x * 2, numbers)
#
#
# with TimeIt():
#     print("Time for for loop")
#     doubled = []
#     for x in numbers:
#         doubled.append(x * 2)

# ======================================================================================================================

# filter() function
# "filter()" ia parametrii
# o functie lambda care returneaza True sau False
# si lista pe care aplicam operatia
odd_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(odd_numbers)

# ======================================================================================================================

# reduce() function
# "reduce()" ca returna o singura valoare
from functools import reduce


sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)
