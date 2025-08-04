numbers = [13, 31, 40, 55]
for number in numbers:
    if number % 8 == 0:
        print("There is an unqualified number in the list")
else:
    # This will execute if the loop completes without a break
    print("All numbers are qualified")
print("End of the program.")
