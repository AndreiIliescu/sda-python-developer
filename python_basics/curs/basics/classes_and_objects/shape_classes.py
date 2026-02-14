from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * self.radius * math.pi


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def perimeter(self):
        return 4 * self.side_length


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)


if __name__ == '__main__':
    circle = Circle(3)
    print(f"circle.perimeter = {circle.perimeter()}")
    square = Square(4)
    print(f"square.perimeter = {square.perimeter()}")
    rectangle = Rectangle(5,7)
    print(f"rectangle.perimeter = {rectangle.perimeter()}")
