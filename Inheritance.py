"""
Author: Zachary Mason
Student ID: W0490903
Course: PROG1400
Date: 2024-01-18
Project: Intro OOP Functions to Classes (Inheritance)
Repository: https://github.com/W0490903/PROG1400/
Programming Language: Python 3
"""

# Animal Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Dog Sub-Class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    
# Cat Sub-Class
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
# Create Objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Use Methods
print(f"{dog.name}")
print(f"{dog.speak()}")
print(f"{cat.name}")
print(f"{cat.speak()}")