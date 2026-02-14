class Dog:
    def speak(self):
        print('Ham ham')


class Cat:
    def speak(self):
        print('Miau miau')


animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()
