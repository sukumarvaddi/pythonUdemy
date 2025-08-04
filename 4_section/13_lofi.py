low = 0
high = 1000

print("Please think of a number between {} and {}.".format(low, high))
input("Press Enter when you are ready...")
guesses = 1

while True:
    print("Guessing a number between {} and {}.".format(low, high))
    guess = low + (high-low)//2
    print("Is your number {}?".format(guess))
    response = input(
        "Enter 'h' if the number is higher, 'l' if it is lower, or 'c' if I guessed correctly: ".casefold())
    if response == 'c':
        print("Yay! I guessed your number in {} tries and the guess is {}.".format(
            guesses, guess))
        break
    elif response == 'h':
        high = guess - 1
    elif response == 'l':
        low = guess + 1
    else:
        print("Invalid input. Please enter 'h', 'l', or 'c'.")
    guesses += 1
