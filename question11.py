class Payroll:
    def __init__(self):  # Corrected the constructor
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_payroll(self):
        total_payroll = 0
        for employee in self.employees:
            # Assuming each employee has a method calculate_salary that returns a salary value
            total_payroll += employee.calculate_salary()
        return total_payroll

# Example Employee class for demonstration
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

# Example usage
payroll = Payroll()
payroll.add_employee(Employee("Alice", 50000))
payroll.add_employee(Employee("Bob", 60000))

total_payroll = payroll.calculate_total_payroll()
print(f"Total Payroll: ${total_payroll}")  # Output: Total Payroll: $110000