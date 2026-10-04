# Module 12 - Project 4: Classes and Program Structure
# The game uses the Player, Room and Item classes from the game package

from game.item import Item
from game.room import Room
from game.player import Player


def show_menu():
    print("\n=== MAIN MENU ===")
    print("look - look around")
    print("move - move to another place")
    print("collect - collect the item here")
    print("inventory - show your inventory")
    print("lopeta - quit the game")


def look(player):
    print(f"You are at the {player.location.name}.")
    if player.location.item is None:
        print("There is nothing here.")
    else:
        print(f"There is an item here: {player.location.item.name}")


def move(player, rooms):
    for i in range(len(rooms)):
        print(f"{i + 1}. {rooms[i].name}")
    choice = input("Where do you want to go? ")
    if choice.isdigit() and 1 <= int(choice) <= len(rooms):
        player.move(rooms[int(choice) - 1])
    else:
        print("There is no such place.")


def show_inventory(player):
    if len(player.items) == 0:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        total = 0
        for item in player.items:
            print(f"- {item.name} ({item.weight} kg)")
            total += item.weight
        print(f"Total weight: {total:.1f} kg")


player_name = input("Enter your name: ")
player_age = int(input("Enter your age: "))

if player_age < 12:
    print("You are a minor. The game will now close.")
else:
    lantern = Item("lantern", 1.5)
    rope = Item("rope", 2.0)
    old_map = Item("old map", 0.1)

    forest_path = Room("forest path")
    cabin = Room("old cabin", lantern)
    cave = Room("dark cave", rope)
    river = Room("river bank", old_map)
    rooms = [forest_path, cabin, cave, river]

    player = Player(player_name, player_age, forest_path)

    print(f"\nWelcome, {player.name}!")
    print(f"You are {player.age} years old.")
    print("Your adventure begins now...")

    command = ""
    while command != "lopeta":
        show_menu()
        command = input("Enter command: ").lower()

        if command == "look":
            look(player)
        elif command == "move":
            move(player, rooms)
        elif command == "collect":
            player.collect_item()
        elif command == "inventory":
            show_inventory(player)
        elif command == "lopeta":
            print(f"Thanks for playing, {player.name}! Goodbye!")
        else:
            print("Unknown command. Try again.")
