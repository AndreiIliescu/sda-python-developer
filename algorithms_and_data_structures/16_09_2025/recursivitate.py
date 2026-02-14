# Metoda 1 - recursiune
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1) # Functa se apeleaza recursiv: functia se apeleaza pe ea insasi


print(factorial(5)) # 1 * 2 * 3 * 4 * 5

print()

# Metoda 2 - iterativ, cu for loop
def factorial_iterative_with_for_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial_iterative_with_for_loop(5))

print()

# Metoda 3 - iterativ, cu while loop
def factorial_iterative_with_while_loop(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result


print(factorial_iterative_with_while_loop(5))

print()

# Metoda 4 - cu modulul math
import math


def factorial_with_math_module(n):
    return math.factorial(n)


print(factorial_with_math_module(5)) # Functia "factorial" din modulul "math" nu foloseste recursivitate, ci foloseste iteratii
