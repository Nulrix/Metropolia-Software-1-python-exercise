# Module 5 - Exercise 4: Number Guessing Game
# Computer draws random number 1-10, user guesses until correct

import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number (1-10): "))
    
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")
        break
