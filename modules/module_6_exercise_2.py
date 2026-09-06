# Module 6 - Exercise 2: Top 5 Greatest Numbers
# Asks user to enter numbers until empty string, prints 5 greatest sorted descending

numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    
    if user_input == "":
        break
    
    numbers.append(float(user_input))

if numbers:
    # Sort in descending order and take first 5
    numbers.sort(reverse=True)
    top_five = numbers[:5]
    
    print("\nTop 5 greatest numbers:")
    for number in top_five:
        print(number)
else:
    print("No numbers were entered.")
