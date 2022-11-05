# This is the simplest one of all the python calculators.
num23 = input("Enter a number: ")
num24 = input("Enter another number: ")
op = input("Select an operator from the following: Add, Multiply, Divide, Minus: ")
# I don't know why I chose num23 and 24

def multiply(num1, num2):
    print(int(num1) * int(num2))

def add(num1, num2):
    print(int(num1) + int(num2))

def divide(num1, num2):
    print(int(num1) / int(num2))

def minus(num1, num2):
    print(int(num1) - int(num2))


if op == 'Multiply':
    multiply(num23, num24)

elif op == 'Add':
    add(num23, num24)

elif op == 'Divide':
    divide(num23, num24)

elif op == 'Minus':
    minus(num23, num24)

else:
    print("Invalid entry!")