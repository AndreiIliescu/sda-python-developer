import timeit
from functools import lru_cache


### Fibonacci ###

# Secventa Fibonacci = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

# Implementarea iterativa pt. calcularea elementului "n", din secventa Fibonacci
def fib_iter(n: int) -> int:
    first_number, second_number = 0, 1
    for i in range(1, n - 1):
        first_number, second_number = second_number, first_number + second_number
    return second_number # Second number contine elementul Fibonacci de pe pozitia n


# print(fib_iter(1))
# print(fib_iter(5)) # Calculam al 5-lea element
# print(fib_iter(10)) # Calculam al 10-lea element

# Implementarea recursiva pt. calcularea elementului "n" din secventa Fibonacci
def fib_rec(n: int) -> int:
    if n < 1:
        return 0
    elif n < 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


# print(fib_rec(1))
# print(fib_rec(5))
# print(fib_rec(10))

n = 4
print("Fara cache: ")
print(timeit.timeit("fib_rec(n)", "from __main__ import fib_rec, n", number=10))
print(timeit.timeit("fib_iter(n)", "from __main__ import fib_iter, n", number=10))
# Ce ne arata in consola: 1.69...e - 05 => 1.69 * 10^-5
# Ce ne arata in consola: 8.79...e - 06 => 8.79 * 10^-6
# Timpul pentru fir_rec = 0.0000169... -> este mai lent
# Timpul pentru fir_iter = 0.00000879... -> este mai rapid
print()

@lru_cache(maxsize=32)
def fib_rec_cache(n: int) -> int:
    if n < 1:
        return 0
    elif n < 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


@lru_cache(maxsize=32)
def fib_iter_cache(n: int) -> int:
    first_number, second_number = 0, 1
    for i in range(1, n - 1):
        first_number, second_number = second_number, first_number + second_number
    return second_number


print("Cu cache: ")
print(timeit.timeit("fib_rec_cache(n)", "from __main__ import fib_rec_cache, n", number=10))
print(timeit.timeit("fib_iter_cache(n)", "from __main__ import fib_iter_cache, n", number=10))
# Folosind cache:
# 1.39 * 10^-5
# 1.49 * 10^-6
# Decoratorul "@lru_cache" memoreaza rezultatele functiilor pt. anumite argumente, ca sa nu le recalculam de fiecare data
# LRU = Least Recently Used -> daca cache-ul este plin, sterge rezultatul cel mai vechi/neutilizat
