# Module 5 - Exercise 3: Find Smallest and Largest Number
# Asks user to enter numbers until empty string, then prints min and max

numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    
    if user_input == "":
        break
    
    numbers.append(float(user_input))

if numbers:
    smallest = min(numbers)
    largest = max(numbers)
    
    print(f"\nSmallest number: {smallest}")
    print(f"Largest number: {largest}")
else:
    print("No numbers were entered.")
