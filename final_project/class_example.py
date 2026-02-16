class Animal:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name


a = Animal("Rex")
print(a)
