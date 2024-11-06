class Cat:
    def make_sound(self):
        print("Meow")

class Dog:
    def make_sound(self):
        print("Woof")

def animal_sound(animal):
    animal.make_sound()

# Demonstrating polymorphism
cat = Cat()
dog = Dog()
animal_sound(cat)
animal_sound(dog)