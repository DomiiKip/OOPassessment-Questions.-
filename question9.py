class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Testing the Vector class and operator overloading
vector1 = Vector(2, 3)
vector2 = Vector(5, 7)

result_vector = vector1 + vector2
print(f"Result of vector addition: {result_vector}")  # Output: Result of vector addition: Vector(7, 10)