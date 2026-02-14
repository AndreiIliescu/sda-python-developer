### Abstract classes ###
from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Implementarea functiei perimeter
    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.length * self.width

    # Functia "__eq__" este folosita automat de Python atunci cand compara doua obiecte
    # (Atunci cand folosim operatorul "==")
    def __eq__(self, other):
        return (self.width, self.length) == (other.width, other.length)


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * self.radius * pi

    def area(self):
        return pi * self.radius ** 2

rect = Rectangle(10, 5)
print(f"Rect perimeter is {rect.perimeter()}\n")

circle = Circle(8)
print(f"Circle area is {circle.area()}\n")

my_rect1 = Rectangle(5, 5)
my_rect2 = Rectangle(5, 7)
print(my_rect1 == my_rect2)
