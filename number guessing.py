import random 

print("Welcome to guess the number!")
print("I am thinking of a number from 1 to 50")

secret = random.radint (1,50)
attempts = 0

while True:
    guess = int(input("Enter your guess:"))
    attempts = 1 

    if guess <1 or guess >50:
        print("Please enter a number from1 to 50")
    elif guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed it in { attempts } , attempts.")

        print("Please enter a whole number.")

        print("Thanks for playing.")
