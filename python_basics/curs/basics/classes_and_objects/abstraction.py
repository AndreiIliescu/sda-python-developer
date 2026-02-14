import abc


class Entity(abc.ABC):
    @abc.abstractmethod
    def speak(self, a, b, c):
        pass


class Animal(abc.ABC):
    @abc.abstractmethod
    def speak(self, b):
        pass


class Dog(Animal, Entity):
    def speak(self, a):
        print('ham ham')


class Cat(Animal):
    def speak(self):
        print('miau miau')


a = Animal()
print(a)
