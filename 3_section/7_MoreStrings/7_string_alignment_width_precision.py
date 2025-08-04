for i in range(1, 13):
    print("No {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))

    # Right alignment
for i in range(1, 13):
    print("No {0} squared is {1:3} and cubed is {2:4}".format(i, i**2, i**3))

    # Center alignment
for i in range(1, 13):
    print("No {0} squared is {1:^3} and cubed is {2:^4}".format(i, i**2, i**3))
    # Left alignment
for i in range(1, 13):
    print("No {0} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i**3))

# Default precision: 15 numbers after decimal point
print("PI is approximately {0}".format(22/7))
# Prints 6 numbers after decimal point with the width enough for 12 numbers
print("PI is approximately {0:12f}".format(22/7))
# Prints 50 numbers after decimal point with the width enough for 12 numbers. Because we cannot print 50 numbers after decimal point with the width enough for 12 numbers, it will print 50 numbers after decimal points
print("PI is approximately {0:12.50f}".format(22/7))

# Prints 50 numbers after decimal point with the width enough for 62 numbers with the default alignment (right).
print("PI is approximately {0:62.50f}".format(22/7))

# Prints 50 numbers after decimal point with the width enough for 62 numbers with the left alignment.
print("PI is approximately {0:<62.50f}".format(22/7))

print("Month {0:02d}".format(4))
