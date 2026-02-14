# Functii lambda pentru "sorted()", "min()", "max()"

# nums = [1, 4, 10, 8, 12]

# print(sorted(nums))
# print(min(nums))
# print(max(nums))

pairs = [(1, 10, 5), (2, 9, 100), (3, 8, 0)]

# Primul element din tuple este folosit la comparare
print("Fara functii lambda:")
print(sorted(pairs))
print(min(pairs))
print(max(pairs))
print("\n")

# Folosim lambda functions pentru a schimba elementul comparat
print("Cu functii lambda:")
print(sorted(pairs, key=lambda x: x[2]))
print(min(pairs, key=lambda x: x[2]))
print(max(pairs, key=lambda x: x[2]))
