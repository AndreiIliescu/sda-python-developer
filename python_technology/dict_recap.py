person = {
    "name": "Marius",
    "age": 24,
    "city": "Bucuresti",
}

print(person["name"])

# Sters key din dictionar
del person["city"]
print(person)

person["height"] = "1.61" # Daca key nu exista deja, va fi creat si adaugat in disctionar
person["name"] = 'Andrei' # Modifica o valoare existenta

# Functii utile
print(person.keys())
print(person.values())
print(person.items())

# Parcurs dictionarul
for key, value in person.items():
    print(f"Cheia este {key} si valoare ei: {value}")

new_dict = person | {"name": 'nume'}
person |= {"name": 'nume'}
