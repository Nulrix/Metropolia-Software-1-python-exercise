# Module 5 - Exercise 5: Login System
# Asks for username and password with max 5 attempts
# Correct username: python, password: rules

CORRECT_USERNAME = "python"
CORRECT_PASSWORD = "rules"
MAX_ATTEMPTS = 5

attempts = 0

while attempts < MAX_ATTEMPTS:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print("Welcome")
        break
    else:
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts
        
        if remaining > 0:
            print(f"Invalid credentials. {remaining} attempts remaining.\n")
        else:
            print("Access denied")
