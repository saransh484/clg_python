try:
    roll = int(input("Please enter your roll number"))
    if roll <= 0:
        raise ValueError()
except ValueError:
    print("ValueError Exception thrown")

print("Outside of try-except clauses.")
