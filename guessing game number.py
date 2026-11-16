
import random

playing = True

# Generate a random number between 0 and 9
number = random.randint(0, 9)

print("The computer has generated a random number.")
print("You have to guess the number between 0 and 9.")

while playing:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("You win the game!")
        print("The correct number was:", number)
        break
    else:
        print("Your guess isn't quite right, try again.")
