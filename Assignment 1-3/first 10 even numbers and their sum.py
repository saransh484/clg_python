# first 10 even number and their sum using while loop

i = 1
total = 0

print("first 10 even numbers are:")
while i<=10:
    print(2*i)
    total = total + (2*i)
    i = i+1

print("sum of first 10 even numbers is :",total)
