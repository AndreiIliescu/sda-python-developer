### Metode magice (__init__, __str__, __repr__, etc.)
# __init__ este constructorul clasei.
# __str__ definește reprezentarea prietenoasă pentru print().
# __repr__ definește reprezentarea oficială.
# Exemplu:
class Animal:
    def __init__(self, nume="Rex", varsta=2):
        self.nume = nume
        self.varsta = varsta
    def __str__(self):
        return f"<{self.nume} ({self.varsta} ani)>"

a = Animal("Lulu", 5)
print(a)  # <Lulu (5 ani)>
