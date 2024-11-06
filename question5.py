class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width is not None else length  # Assume square if width is not provided

    def area(self):
        return self.length * self.width

# Testing constructor overloading
square = Rectangle(5)        # This creates a square with length and width of 5
rectangle = Rectangle(5, 10)  # This creates a rectangle with length 5 and width 10

print("Square area:", square.area())        # Output: Square area: 25
print("Rectangle area:", rectangle.area())  # Output: Rectangle area: 50