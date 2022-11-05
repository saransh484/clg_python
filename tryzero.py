a = 10
b = 0
try:
    c = a/b
except:
    print("cant divide by zero \n try to divide by the value other than zero")
print("---------------")

a = 'Saransh'
b = 10
try:
    c = a/b
except (NameError, TypeError) as error:
    print(error)
