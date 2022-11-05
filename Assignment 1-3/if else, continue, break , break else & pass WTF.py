# using if else, continue, break , else & pass statement using for loop

x = int(input("enter a number : " ))

for i in range(20):

    if i == 0:
        continue

    if i > 10:
        break
    
    else:
        pass
    
    print("{} * {} = {}".format(x, i, x*i))



    

    

