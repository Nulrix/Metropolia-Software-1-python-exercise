# Module 6 - Exercise 1: Dice Roller
# Asks user how many dice to roll, rolls them all and prints the sum

import random

num_dice = int(input("How many dice to roll? "))

total_sum = 0

for i in range(num_dice):
    roll = random.randint(1, 6)
    print(f"Die {i+1}: {roll}")
    total_sum += roll

print(f"\nTotal sum: {total_sum}")
