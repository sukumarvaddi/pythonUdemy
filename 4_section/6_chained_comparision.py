age = int(input("What is your age?"))
if 16 <= age <= 65:
    print("You are eligible to work")
else:
    print("You can relax")

print("_" * 80)
if age < 16 or age > 65:
    print("You can relax")
