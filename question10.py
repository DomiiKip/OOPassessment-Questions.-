from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Creating instances of Circle and Square
circle = Circle(5)
square = Square(4)

# Calling area() on each
print(f"Area of the circle: {circle.area():.2f}")  
print(f"Area of the square: {square.area()}")