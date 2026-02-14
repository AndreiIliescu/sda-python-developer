from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Oras:
    name: str
    population: int
    area: float


oras1 = Oras("Cluj", 300, 1000)

my_list = [1, 5, 45, oras1]

# Un shallow copy va copia referinta obiectelor din interior
shallow_copy_list = list(my_list)

# Un deep copy va crea o copie a obiectelor din lista
deep_copy_list = deepcopy(my_list)

# Daca modificam o proprietate a unui obiect intr-un shallow copy
# Schimbarile vor aparea si in lista originala
shallow_copy_list[0] = "text"
shallow_copy_list[3].name = "Bacau"

print(f"Original: {my_list}\n")
print(f"Shallow copy: {shallow_copy_list}\n")
print(f"Deep copy: {deep_copy_list}\n")
print(f"City name: {deep_copy_list[3].name}\n")
