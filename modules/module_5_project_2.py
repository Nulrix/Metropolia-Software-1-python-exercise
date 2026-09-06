# Module 5 - Project 2: Game with Main Menu
# Asks for player name and age, checks if minor
# Displays main menu with commands until user enters "lopeta"

player_name = input("Enter your name: ")
player_age = int(input("Enter your age: "))

if player_age < 12:
    print("You are a minor. Access denied.")
else:
    print(f"\nWelcome, {player_name}!")
    print(f"You are {player_age} years old.\n")
    
    while True:
        print("=== MAIN MENU ===")
        print("1. start - Start the adventure")
        print("2. status - Check your status")
        print("3. inventory - View your inventory")
        print("4. help - Get help")
        print("5. lopeta - Exit the game")
        
        command = input("\nEnter command: ").lower()
        
        if command == "start" or command == "1":
            print("Your adventure begins in a dark forest...\n")
        elif command == "status" or command == "2":
            print(f"Player: {player_name}, Age: {player_age}, Level: 1\n")
        elif command == "inventory" or command == "3":
            print("Inventory: Sword, Shield, Health Potion\n")
        elif command == "help" or command == "4":
            print("Type a command to perform an action. Type 'lopeta' to quit.\n")
        elif command == "lopeta" or command == "5":
            print(f"Thanks for playing, {player_name}! Goodbye!")
            break
        else:
            print("Unknown command. Try again.\n")
