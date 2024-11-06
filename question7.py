class Engine:
    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")

class Car:
    def __init__(self):  # Corrected constructor name
        self.engine = Engine()  # Engine instance as part of Car

    def start_car(self):
        self.engine.start()

    def stop_car(self):
        self.engine.stop()

# Using composition
my_car = Car()
my_car.start_car()
my_car.stop_car()