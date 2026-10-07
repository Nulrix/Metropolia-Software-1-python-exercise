# Module 13 - Project 5: File Handling
# Reads the intro and instructions from text files and saves the game so it can be continued later

from game.item import Item
from game.room import Room
from game.player import Player
from game.file_handling import read_text_file, save_exists, save_game, load_game


def show_menu():
    print("\n=== MAIN MENU ===")
    print("look - look around")
    print("move - move to another place")
    print("collect - collect the item here")
    print("inventory - show your inventory")
    print("save - save the game")
    print("help - show the instructions")
    print("lopeta - quit the game")


def create_rooms():
    lantern = Item("lantern", 1.5)
    rope = Item("rope", 2.0)
    old_map = Item("old map", 0.1)

    forest_path = Room("forest path")
    cabin = Room("old cabin", lantern)
    cave = Room("dark cave", rope)
    river = Room("river bank", old_map)
    return [forest_path, cabin, cave, river]


def ask_age():
    age = input("Enter your age: ")
    while not age.isdigit():
        age = input("Enter your age as a number: ")
    return int(age)


def start_game(rooms):
    # returns the player, or None if the player is too young to play
    player_name = input("Enter your name: ")

    if save_exists(player_name):
        answer = input(f"A saved game was found for {player_name}. Continue it? (y/n): ").lower()
        if answer == "y":
            player = load_game(player_name, rooms)
            print(f"\nWelcome back, {player.name}! You are at the {player.location.name}.")
            return player
        print("Starting a new game.")

    player_age = ask_age()
    if player_age < 12:
        print("You are a minor. The game will now close.")
        return None

    player = Player(player_name, player_age, rooms[0])
    print(f"\nWelcome, {player.name}!")
    print(f"You are {player.age} years old.")
    print("Your adventure begins now...\n")
    print(read_text_file("instructions.txt"))
    return player


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


print(read_text_file("intro.txt"))

rooms = create_rooms()
player = start_game(rooms)

if player is not None:
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
        elif command == "save":
            save_game(player)
            print("The game was saved. Enter the same name next time to continue.")
        elif command == "help":
            print(read_text_file("instructions.txt"))
        elif command == "lopeta":
            answer = input("Do you want to save before quitting? (y/n): ").lower()
            if answer == "y":
                save_game(player)
                print("The game was saved.")
            print(f"Thanks for playing, {player.name}! Goodbye!")
        else:
            print("Unknown command. Try again.")
