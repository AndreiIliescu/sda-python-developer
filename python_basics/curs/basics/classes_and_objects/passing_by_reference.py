class Animal:
    def __init__(self, name="Rex", age=2):
        self.name = name
        self.age = age


dog_a = Animal()
dog_b = dog_a
print(dog_a.name)  # Return "Rex"
print(dog_b.name)  # Return "Rex"

dog_a.name = "Pongo"
print(dog_a.name)  # Return "Pongo"
print(dog_b.name)  # Return "Pongo"


print(dog_a)
print(dog_b)
