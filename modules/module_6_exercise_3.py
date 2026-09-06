# Module 6 - Exercise 3: Prime Number Checker
# Asks user for an integer and tells if it's a prime number

number = int(input("Enter an integer: "))

if number < 2:
    print(f"{number} is not a prime number.")
else:
    is_prime = True
    
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
