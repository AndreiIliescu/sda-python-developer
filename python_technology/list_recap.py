my_list = [10, 'a', True, 4.3]

my_list[0] # -> 10
my_list[3] # -> 4.3

# Index cu "-" inseamna ca va porni din dreapta listei
my_list[-1] # -> 4.3

# List slicing
print(my_list[1:3])

# Parcurs lista
for element in my_list:
    print(f"elementul este: {element}")

print(len(my_list))

# adaugat element in lista
my_list.append(10)

# scos un element din lista
e = my_list.pop(-1)
print(e)

# extins lista
my_list.extend([1, 2])
print(my_list)

print('acesta', 'este', 'un', 'string', sep='-', end='8')
print('randul 2')
