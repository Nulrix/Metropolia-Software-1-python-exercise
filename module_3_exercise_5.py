# Module 3 - Exercise 5: Medieval Weight Converter
# Converts medieval units (talents, pounds, lots) to kilograms and grams

# Conversion factors
LOTS_PER_GRAM = 13.3
LOTS_PER_POUND = 32
POUNDS_PER_TALENT = 20

# Ask for user input
talents = float(input("Enter talents:\n"))
pounds = float(input("Enter pounds:\n"))
lots = float(input("Enter lots:\n"))

# Convert everything to lots
total_lots = (talents * POUNDS_PER_TALENT * LOTS_PER_POUND) + (pounds * LOTS_PER_POUND) + lots

# Convert lots to grams
total_grams = total_lots * LOTS_PER_GRAM

# Convert grams to kilograms and remaining grams
kilograms = int(total_grams // 1000)
remaining_grams = total_grams % 1000

print(f"\nThe weight in modern units:")
print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")
