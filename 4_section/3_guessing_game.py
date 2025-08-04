answer = 5
print("Please guess a number between 1 and 10")
guess = int(input())
if guess < answer:
    print("Guess higher")
elif guess > answer:
    print("Guess lower")
else:
    print("You guessed it!")
