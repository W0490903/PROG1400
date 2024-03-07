### Task 1: Abstraction ###

# Define Shape class.
class Shape:
    def __str__(self) -> str:
        return self.__class__.__name__

# Define Rectangle class with inheritance from the Shape class.
class Rectangle(Shape):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    # Implement method to calculate area.
    def calculate_area(self):
        return self.length * self.width
    
# Define Circle class with inheritance from the Shape class.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    # Implement abstract method to calculate area.
    def calculate_area(self):
        return (3.14 * self.radius ** 2)
    
# Define a polymorpic function to calculate the area of any shape passed.
def print_area(shape):
    print(f"The area of the {shape} is {shape.calculate_area()}.")



### Task 2: Encapsulation ###

# Define Student class.
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # Create method to return the student's grade.
    def get_grade(self):
        return self.grade
    
    # Create method to change grade.
    def change_grade(self, new_grade):
        self.grade = new_grade
        
# Create function to print the student's current grade.    
def print_grade(student):
    print(f"{student.name}'s grade is: {student.get_grade()}")

# Create function to prompt user for new grade, then change student's grade.
def change_grade(student):
    new_grade = input(f"Please enter new grade for {student.name}: ")
    student.change_grade(new_grade)
    print(f"Grade changed successfully. {student.name}'s new grade is: {student.grade}")



### Task 3: Inheritance ###

# Define Animal Class.
class Animal:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def speak(self):
        return

    def move(self):
        return f"{self.name} the {self.colour} {self} walks on four legs"

    def __str__(self):
        return self.__class__.__name__
    
    

# Define Cat sub-class.
class Cat(Animal):
    def speak(self):
        return f"{self.name} the {self.colour} {self} says Meow."
        
# Define Dog sub-class.
class Dog(Animal):
    def speak(self):
        return f"{self.name} the {self.colour} {self} says Woof."

# Define Bird sub-class.    
class Bird(Animal):
    def speak(self):
       return f"{self.name} the {self.colour} {self} says Chirp-chirp."
    
    def move(self):
        return f"{self.name} the {self.colour} {self} walks on two legs and can even fly!"
        
    
# Create function to make the animal speak.
def speak(animal):
    print(animal.speak())

def move(animal):
    print(animal.move())



### Task 4: Polymorphism ###

# Define the Vehicle class.
class Vehicle:
    def __init__(self, colour):
        self.colour = colour

    def travel(self):
        pass

    def __str__(self) -> str:
        return self.__class__.__name__

# Define the Car sub-class.
class Car(Vehicle):
    def travel(self):
        return f"A {self.colour} {self} travels quickly to it's destination."

# Define the Plane sub-class.
class Plane(Vehicle):
    def travel(self):
        return f"A {self.colour} {self} travels very quickly to it's destination."

# Define the Bicycle sub-class.
class Bicycle(Vehicle):
    def travel(self):
        return f"A {self.colour} {self} travels slowly to it's destination."

# Define a travel function to display the vehicle's travel info. 
def travel(vehicle):
    print(vehicle.travel())

# Create a run function to individually run each selected task section.
def run(objects):
    for obj in objects:
        if isinstance(obj, Shape):
            print_area(obj)
        elif isinstance(obj, Student):
            print_grade(obj)
            change_grade(obj)
        elif isinstance(obj, Animal):
            speak(obj)
            move(obj)
        elif isinstance(obj, Vehicle):
            travel(obj)

shape_objects = [Rectangle(3, 5, 2), Circle(2)]
student_objects = [Student('Zach', 29, 88), Student('Alice', 22, 75)]
animal_objects = [Cat("Whiskers", "Orange"), Dog("Bones", "Brown"), Bird("Sonny", "Blue")]
vehicle_objects = [Car("blue"), Plane("white"), Bicycle("green")]

#run(shape_objects)
#run(student_objects)
#run(animal_objects)
#run(vehicle_objects)