### Tuple
# Colecție ordonată, indexată, dar imuabilă (nu se poate modifica după creare).
# Definire prin paranteze sau virgule:
t = (10, 20, 30)
print(t[1])


# Exemplu 2: dezambalare (unpacking):
(a, b, c) = t
print(a, b, c)


# Exemplu 3:
tup = (10, 20, 20, 30)
print("Tuplu:", tup)
print("Tuplu[1]:", tup[1], "len(tup):", len(tup))
print("Count(20):", tup.count(20))
print("Indexul lui 30:", tup.index(30))
# Nu putem face tup.append(), deoarece tuplurile sunt imutabile.
