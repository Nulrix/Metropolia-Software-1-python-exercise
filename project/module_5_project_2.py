# Module 5 - Project 2: Main Menu
# Checks the player's age and shows the main menu until the player enters "lopeta"

player_name = input("Enter your name: ")
player_age = int(input("Enter your age: "))

if player_age < 12:
    print("You are a minor. The game will now close.")
else:
    print(f"\nWelcome, {player_name}!")
    print(f"You are {player_age} years old.")
    print("Your adventure begins now...")

    command = ""
    while command != "lopeta":
        print("\n=== MAIN MENU ===")
        print("explore - explore the forest")
        print("status - show your status")
        print("rest - rest by the campfire")
        print("lopeta - quit the game")
        command = input("Enter command: ").lower()

        if command == "explore":
            print("You walk deeper into the dark forest. Something moves in the bushes...")
        elif command == "status":
            print(f"Player: {player_name}, Age: {player_age}, Health: 100")
        elif command == "rest":
            print("You sit by the campfire and feel rested.")
        elif command == "lopeta":
            print(f"Thanks for playing, {player_name}! Goodbye!")
        else:
            print("Unknown command. Try again.")
