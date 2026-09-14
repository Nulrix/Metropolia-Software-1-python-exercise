# Module 7 - Exercise 1: Dice Roll
# Program that rolls a six-sided dice until the result is 6

import random


def roll_dice():
    return random.randint(1, 6)


result = 0
while result != 6:
    result = roll_dice()
    print(result)

print("You got a six!")
