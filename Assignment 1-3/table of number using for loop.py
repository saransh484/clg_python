# table of any number using for loop

x = int(input("Enter number to find table of : "))

i = 1

for i in range(1,11):
    print("{} x {} = {}".format(x, i, x*i))
    i = i + 1
