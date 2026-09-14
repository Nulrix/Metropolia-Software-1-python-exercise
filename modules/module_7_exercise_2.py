# Module 7 - Exercise 2: Dice Roll With Any Number Of Sides
# Program that rolls a dice until the maximum value is rolled

import random


def roll_dice(sides):
    return random.randint(1, sides)


sides = int(input("How many sides does the dice have? "))

result = 0
while result != sides:
    result = roll_dice(sides)
    print(result)

print(f"You got the maximum value {sides}!")
