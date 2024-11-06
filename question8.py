class Calculator:
    count = 0  # Static attribute to track the number of times add() is called

    @staticmethod
    def add(a, b):
        Calculator.count += 1  # Increment the count each time add() is called
        return a + b

# Using the Calculator class
result1 = Calculator.add(5, 3)
print(f"Result of addition: {result1}")  # Output: Result of addition: 8
print(f"Add method called: {Calculator.count} times")  # Output: Add method called: 1 times

result2 = Calculator.add(10, 20)
print(f"Result of addition: {result2}")  # Output: Result of addition: 30
print(f"Add method called: {Calculator.count} times")  # Output: Add method called: 2 times