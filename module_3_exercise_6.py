# Module 3 - Exercise 6: Random Combination Lock Generator
# Generates random codes for two types of combination locks

import random

# Generate 3-digit code (0-9)
code_3digit = ""
for i in range(3):
    code_3digit += str(random.randint(0, 9))

# Generate 4-digit code (1-6)
code_4digit = ""
for i in range(4):
    code_4digit += str(random.randint(1, 6))

print("Combination lock codes:")
print(f"3-digit code (0-9): {code_3digit}")
print(f"4-digit code (1-6): {code_4digit}")
