import random


def show_menu():
    print()
    print("Commands:")
    print("pick - pick up an item")
    print("inv - show inventory")
    print("look - look around")
    print("rest - rest for a while")
    print("lopeta - quit")


def pick_up_item(inventory):
    item = input("What do you want to pick up? ").strip()
    if item == "":
        print("You didn't pick up anything.")
    else:
        inventory.append(item)
        print(f"You put the {item} in your backpack.")


def show_inventory(inventory):
    if len(inventory) == 0:
        print("Your backpack is empty.")
    else:
        print("Your backpack has:")
        for item in inventory:
            print(item)


def look_around():
    sights = ["Servers are blinking in the dark.",
              "There is a broken monitor in the corner.",
              "Cables are hanging from the ceiling.",
              "Someone left a sticky note on the wall that says password123."]
    print(random.choice(sights))


def rest(name):
    print(f"{name} sits down on the floor and takes a break.")


player_name = input("Enter your name: ")
age = input("Enter your age: ")
while not age.isdigit():
    age = input("Enter your age as a number: ")
player_age = int(age)

if player_age < 12:
    print("You are a minor, so you can't play this game.")
else:
    print(f"Hello {player_name}, welcome to Escape from the Server Room!")
    inventory = []
    command = ""
    while command != "lopeta":
        show_menu()
        command = input("Enter command: ").strip().lower()
        if command == "pick":
            pick_up_item(inventory)
        elif command == "inv":
            show_inventory(inventory)
        elif command == "look":
            look_around()
        elif command == "rest":
            rest(player_name)
        elif command == "lopeta":
            print("Bye!")
        else:
            print("Unknown command.")
