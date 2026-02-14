### Decoratorul @dataclass ###
from dataclasses import dataclass


# class Oras:
#     def __init__(self, name, population, area):
#         self.name = name
#         self.population = population
#         self.area = area
#
#     def __str__(self):
#         return f"{self.name}, {self.population}, {self.area}"
#
#     def __eq__(self, other):
#         return (self.name, self.population, self.area) == (other.name, other.population, other.area)

# Sau folosim decoratorul "@dataclass"
# El va genera automat metodele "__init__", "__eq__", "__repr__"
@dataclass
class Oras:
    name: str
    population: int
    area: float


oras1 = Oras("Bucuresti", 190, 369)
oras2 = Oras("Cluj", 300, 128)
oras3 = Oras("Bucuresti", 190, 369)

print(oras1)
print(oras1 == oras2)
print(oras1 == oras3)
