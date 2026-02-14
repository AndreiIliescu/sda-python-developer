import timeit
from functools import lru_cache


# Calcularea factorial folosind programarea dinamica (memorization)
# memory = un dictionar care retine rezultatele deja calculate, e actualizat la fiecareapel al functiei

def factorial(n, memory={0: 1, 1: 1}):
    if n in memory:
        return memory[n]
    else:
        memory[n] = n * factorial(n - 1)
        return memory[n]


print(factorial(5))
print(factorial(6))
print(factorial(10))

print()

n = 5

print("Fara cache: ")
print(timeit.timeit("factorial(n)", "from __main__ import factorial, n", number=10))

print()

# Exemplul de mai sus, doar ca folosim "@lru_cache" + recursivitate
# Decoram functia "factoial" ca sa aiba un cache (o memorie)
@lru_cache(maxsize=32)
def factorial_cache(n, memory={0: 1, 1: 1}):
    if n in memory:
        return memory[n]
    else:
        memory[n] = n * factorial(n - 1)
        return memory[n]


print("Cu cache: ")
print(timeit.timeit("factorial_cache(n)", "from __main__ import factorial_cache, n", number=10))
