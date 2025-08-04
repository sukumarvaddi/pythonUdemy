name = input("What is your name? ")
age = int(input("What is your age {0}? ".format(name)))


if age < 18:
    print("Come back after {0} years.".format(18-age))
elif age == 18:
    print("You are eligible to vote now!")
else:
    print("You are eligible to vote.")
