try:
    a = int(input("enter your age "))
    if a <= 17:
        raise ValueError()
    else:
        print("you are eligible for voting: ")

except ValueError:
    print("LoL he's a noob \U0001F923 \U0001F923 ")
