### Lambda Expressions ###

# Functiile lambda sunt functii anonime (nu le declaram cu "def" urmat de un nume)
# ex.: lambda x: scurt cod care face o operatiune cu x
# x este parametrul functie
# si codul pus dupa doua puncte (":") ca fi returnar de functie

# Exemplul 1:
my_lambda = lambda x: x.lower()
print(my_lambda("HELLO WORLD!"))

# Codul din exemplul 1 este echivalent cu:
# def my_lambda(x):
#     return x.lower()


# print(my_lambda("HELLO WORLD!"))

# Exemplul 2:
square_lambda = lambda a: a ** 2
print(square_lambda(4))

# Exemplul 3:
equals_lambda = lambda x, y: x == y
print(equals_lambda(2, 3)) # -> return False
print(equals_lambda(3, 3)) # -> return True
