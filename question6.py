class Employee:
    def calculate_salary(self):
        print("Calculating generic salary...")

class Manager(Employee):
    def calculate_salary(self):
        print("Calculating manager's salary with bonus...")

# Demonstrating method overriding
manager = Manager()
manager.calculate_salary()