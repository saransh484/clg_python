#swap 2 numbers

print("using temp variable")

num1 = 5
num2 = 10

print("\nbefore swapping")
print("num1 : ", num1)
print("num2 : ", num2)

#swapping
temp = num1
num1 = num2
num2 = temp

print("\nafter swapping")
print("num1 : ", num1)
print("num2 : ", num2)

print("\n \nwithout temp variable")

print("\nbefore swapping")
print("num1 : ", num1)
print("num2 : ", num2)

#swapping
num1, num2 = num2, num1

print("\nafter swapping")
print("num1 : ", num1)
print("num2 : ", num2)
