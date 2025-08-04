answer = 5
print("Please guess a number between  1 and 10")
guess = int(input())

if answer == guess:
    print("You guessed it!")
else:
    if guess < answer:
        print("Guess higher")
    else:
        print("Guess lower")
    guess = int(input())
    if answer == guess:
        print("You guessed it!")
    else:
        print("Sorry, you didn't guess it right.")
