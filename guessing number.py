import random

secret = random.randint(1, 100)

guess = int(input("Guess a number from 1 to 100: "))

while guess != secret:
    if guess < secret:
        print("Too low!")
    else:
        print("Too high!")

    guess = int(input("Guess again: "))

print("You got it! 🎉")