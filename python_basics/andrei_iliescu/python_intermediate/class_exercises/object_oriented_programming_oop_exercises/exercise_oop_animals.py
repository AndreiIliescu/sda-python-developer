class Animals:
    def __init__(self, weight, age):
        self.weight = weight
        self.age = age

    def look(self):
        return "The animal is looking around."

    def breath(self):
        return "The animal is breathing."


class Fish(Animals):
    def __init__(self, weight, age):
        super().__init__(weight, age)

    def swim(self):
        return "The fish is swimming."


class Mammal(Animals):
    def __init__(self, weight, age):
        super().__init__(weight, age)

    def run(self):
        return "The mammal is running."


class Bird(Animals):
    def __init__(self, weight, age):
        super().__init__(weight, age)

    def fly(self):
        return "The bird is flying"


class DomesticDog(Mammal):
    def __init__(self, weight, age, breed, coat_color):
        super().__init__(weight, age)

        self.breed = breed
        self.coat_color = coat_color

    def bark(self):
        return "The dog barks."

    def retrieve(self):
        return "The dog retrieved the ball."
