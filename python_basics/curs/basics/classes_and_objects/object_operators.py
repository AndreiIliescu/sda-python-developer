class Animal:
    def __init__(self, name="Rex", age=2):
        self.name = name
        self.age = age

    def __add__(self, other):
        return Animal(self.name, self.age + int(other))

    def __str__(self):
        return f"<{self.name} ({self.age})>"

    def __int__(self):
        return self.age


print(Animal("Alex", 1) + 1)

print(Animal("Alex", 3) + Animal("Milk", 2))
