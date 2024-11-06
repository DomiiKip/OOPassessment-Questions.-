class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Call the display_info() method
my_car.display_info()