# Module 7 - Project 3: Main Menu Functions and Inventory
# Each menu command is its own function and picked up items are saved in an inventory list

import random


def show_menu():
    print("\n=== MAIN MENU ===")
    print("explore - explore the forest")
    print("pick - pick up an item")
    print("inventory - show your inventory")
    print("drop - drop an item")
    print("lopeta - quit the game")


def explore():
    places = ["an old river", "a dark cave", "a broken bridge", "a quiet clearing"]
    print(f"You walk through the forest and find {random.choice(places)}.")


def pick_up_item(inventory):
    item = input("What item do you pick up? ")
    if item == "":
        print("You did not pick up anything.")
    else:
        inventory.append(item)
        print(f"{item} was added to your inventory.")


def show_inventory(inventory):
    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for item in inventory:
            print(f"- {item}")


def drop_item(inventory):
    item = input("What item do you drop? ")
    if item in inventory:
        inventory.remove(item)
        print(f"You dropped {item}.")
    else:
        print(f"You don't have {item}.")


player_name = input("Enter your name: ")
player_age = int(input("Enter your age: "))

if player_age < 12:
    print("You are a minor. The game will now close.")
else:
    print(f"\nWelcome, {player_name}!")
    print(f"You are {player_age} years old.")
    print("Your adventure begins now...")

    inventory = []
    command = ""
    while command != "lopeta":
        show_menu()
        command = input("Enter command: ").lower()

        if command == "explore":
            explore()
        elif command == "pick":
            pick_up_item(inventory)
        elif command == "inventory":
            show_inventory(inventory)
        elif command == "drop":
            drop_item(inventory)
        elif command == "lopeta":
            print(f"Thanks for playing, {player_name}! Goodbye!")
        else:
            print("Unknown command. Try again.")
