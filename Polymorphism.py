"""
Author: Zachary Mason
Student ID: W0490903
Course: PROG1400
Date: 2024-01-18
Project: Intro OOP Functions to Classes (Polymorphism)
Repository: https://github.com/W0490903/PROG1400/
Programming Language: Python 3
"""
class Fruit:
    # Constructor (__init__ method)
    def __init__(self, name):
        self.name = name

    # Method to return the string "Generic Taste".
    def taste(self):
        return "Generic Taste"
    
class Apple(Fruit):
    def __init__(self, name, colour):
        super().__init__(name) # Call the superclass method.
        self.colour = colour

    def taste(self):
        return (f"{super().taste()} and Crispy!")
    
def describe_taste(fruit):
    print(f"{fruit.name} tastes {fruit.taste()}")

# Create Objects
apple = Apple("Gala", "Red")

print(apple.taste())

# Polymorphism allows you to pass any object to this function to print the taste of the passed object.
describe_taste(apple)