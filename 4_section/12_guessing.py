import random
maximumNumber = 1000
answer = random.randint(1, maximumNumber)

guess = ""

while guess != answer:
    guess = int(
        input("Guess a number between 1 and {0}:".format(maximumNumber)))
    if guess < answer:
        print("Your guess is too low.")
    elif guess == answer:
        print(
            "Congratulations! You guessed the number! The guess is {0}".format(guess))
    else:
        print("Your guess is too high.")
print("The answer was {0}".format(answer))
