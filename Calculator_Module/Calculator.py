# Define a class for Advanced Caluclations
# The @staticmethod decorator is used to define a method within a class 
# that does not access or modify the class or instance state. 
# This means that the method does not have access to the instance (self) 
# or the class (cls) and behaves like a regular function outside the class.
 
# When you define a method within a class, by default it is an instance method, 
# meaning it operates on an instance of the class and has access to the instance 
# attributes via the self parameter. However, sometimes you may want to define a 
# method that does not require access to the instance or the class itself.

class AdvCalculator:
    @staticmethod
    def exponentiate(base, exponent):
        return base ** exponent


# Define functions for basic arithmetic operations.
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

