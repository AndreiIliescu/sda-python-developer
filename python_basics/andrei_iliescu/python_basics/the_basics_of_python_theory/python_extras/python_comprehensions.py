### Comprehensiuni (comprehensions)
# Construirea listelor/dicționarelor/tuplelor dintr-o expresie concisă:
lista = [i*i for i in range(5)]  # [0, 1, 4, 9, 16]
print(lista)
# Dicționar:
dict_cv = {i: chr(65+i) for i in range(3)}  # {0:'A',1:'B',2:'C'}
print(dict_cv)
# Set:
set_cv = {x for x in "abracadabra" if x not in "abc"}
print(set_cv)

### Input și Output
# input() citește de la tastatură (returnează șir).
nume = input("Cum te cheamă? ")
print(f"Salut, {nume}!")  # print() afișează text la ecran.
