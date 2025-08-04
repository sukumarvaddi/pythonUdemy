parrot = "Norwegian Blue"
character = input("Enter a character: ")

if character.casefold() in parrot:
    print("{} is in {}".format(character.casefold(), parrot))
else:
    print("{} is not in {}".format(character, parrot))

print("_" * 80)

if character not in parrot:
    print("{} is not in {}".format(character, parrot))
else:
    print("{} is in {}".format(character, parrot))


# String Methods documentation: https: //docs.python.org/3/library/stdtypes.html#string-methods
