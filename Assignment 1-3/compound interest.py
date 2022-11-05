# calculate compound interest

P = float(input("enter principle amount : "))
R = float(input("enter rate of interest : "))
T = float(input("enter given time : "))

amount = P * (pow((1 + R / 100), T))
ci = amount - P

print("the total amount including compound interest ", amount)
print("the compound interst on the principle amount of ", P, " is ", ci)
