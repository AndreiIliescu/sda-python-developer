class Animal:
    def __init__(self, name="Rex", age=2):
        self.name = name
        self.age = age

    def __str__(self):
        return f"<{self.name} ({self.age})>"

    def __repr__(self):
        # return f"<{self.name}>"
        return str(self)

print(Animal())
print([Animal(), Animal()])
