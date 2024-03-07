import Calculator_Module.Calculator as Calculator

x = int(input("Please enter a number: "))
y = int(input("Please enter a second number: "))


print("Addition:", Calculator.add(x,y))
print("Subtraction:", Calculator.subtract(x,y))
print("Multiplication:", Calculator.multiply(x,y))
print("Division:", Calculator.divide(x,y))
print("Exponentiation:", Calculator.AdvCalculator.exponentiate(x,y))