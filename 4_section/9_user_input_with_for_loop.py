numberWithSeparators = input("Enter a number with separators: ")
separator = ""
for character in numberWithSeparators:
    if not character.isnumeric():
        separator = separator + character

number = "".join(
    char if char not in separator else " " for char in numberWithSeparators).split()
print("The number is: {}".format(number))

print([int(char) for char in number])
