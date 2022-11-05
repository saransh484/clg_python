# largest number among 3

x = int(input("enter 1st number : "))
y = int(input("enter 2nd number : "))
z = int(input("enter 3rd number : "))

if (x > y) & (x > z):
    print("{} is the greatest among {}, {} and {}".format(x ,x, y, z))
elif (y > x) & (y > z):
    print("{} is the greatest among {}, {} and {}".format(y, x, y, z))
else:
    print("{} is the greatest among {}, {} and {}".format(z, x, y, z))
