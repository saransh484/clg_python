# check the number is greater, smaller or equal

x = int(input("enter 1st number : "))
y = int(input("enter 2nd number : "))

if x > y :
    print("the number {} is greater than {}".format(x,y))
elif y > x :
    print("the number {} is smaller than {}".format(x,y))
else:
    print("the number {} are equal {}".format(x,y))
