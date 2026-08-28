# Module 4 - Exercise 1: Zander Fish Size Checker
# Checks if a caught zander meets the minimum size requirement (42 cm)

MIN_SIZE = 42

fish_length = float(input("Enter the length of the zander (in centimeters): "))

if fish_length < MIN_SIZE:
    difference = MIN_SIZE - fish_length
    print(f"Release the fish back into the lake.")
    print(f"The fish is {difference:.1f} centimeters below the size limit.")
else:
    print("The fish meets the size requirement!")
