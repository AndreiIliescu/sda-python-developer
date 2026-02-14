import sys


# Exemplu de recursivitate infinita in Python

# sys.setrecursionlimit(9999999) # Putem modifica limita, dar nu este recomandat (se recomanda o abordare diferita a problemei)

def inf_recursion(number):
    if number != 0:
        print(f"Apel cu number = {number}")
        inf_recursion(number)
    return 0


print(inf_recursion(0)) # Conditia nu e indeplinita ->
print(inf_recursion(1)) # Conditia e indeplinita -> functia se autoapeleaza la nesfarsit

# Python nu permite recursivitate infinita si are o limita implicita
