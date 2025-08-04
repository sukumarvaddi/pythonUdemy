name = input("What is your name? ")
age = int(input("What is your age {0}? ".format(name)))

if age > 18:
    print("You are eligible to vote.")
else:
    print("Come back after {0} years.".format(18-age))

if age < 18:
    print("Come back after {0} years.".format(18-age))
else:
    print("You are eligible to vote.")
