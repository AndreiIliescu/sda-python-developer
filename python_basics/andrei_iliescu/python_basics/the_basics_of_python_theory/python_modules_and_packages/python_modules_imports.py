### Importarea modulelor
# Sintaxa de import:
# - import module
# - import module as alias
# - from module import nume
# - from module import *
import random as rnd
print(rnd.randint(1, 10))
from math import factorial, sqrt
print(factorial(5), sqrt(25))

# random module
# Modulul random oferă funcții pentru generare de valori aleatoare.
# random.random() returnează un float în intervalul [0.0, 1.0): contentReference[oaicite:13]{index=13}.
# random.uniform(a, b) returnează un float aleator între a și b (inclusiv): contentReference[oaicite:14]{index=14}.
# random.choice(seq) alege aleator un element din secvența dată: contentReference[oaicite:15]{index=15}.
# random.shuffle(lst) amestecă aleator elementele listei lst (in-place): contentReference[oaicite:16]{index=16}.

import random

# Exemplu 1: random() și uniform()
print("Random [0,1):", random.random())
print("Random între 5 și 10:", random.uniform(5, 10))

# Exemplu 2: choice și shuffle
lista = [1, 2, 3, 4, 5]
aleator = random.choice(lista)
print("Element ales aleator din listă:", aleator)
random.shuffle(lista)
print("Listă amestecată:", lista)
