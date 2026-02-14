class Animal:
    def __init__(self, name="Rex", age=2):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.age == other.age


print(Animal("Alex", 3) > Animal("Milk", 2))
print(Animal("Alex", 3) == Animal("Milk", 3))
