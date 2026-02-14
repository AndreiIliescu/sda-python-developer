class Bat:
    def __init__(self, species):
        self.species = species


class Man:
    def __init__(self, name):
        self.name = name


class Batman(Bat, Man):
    def __init__(self, name, species):
        Bat.__init__(self, species)
        Man.__init__(self, name)
        print(self.name)
        print(self.species)


batman = Batman('some bat', 'John Wayne')
print(batman)
