def show_menu():
    print()
    print("Commands:")
    print("look - look around")
    print("move - go to another room")
    print("take - pick up the item in the room")
    print("inv - show inventory")
    print("rest - rest for a while")
    print("lopeta - quit")


def look_around(player):
    room = player.location
    print(f"You are in the {room.name}.")
    print(room.description)
    if room.item is not None:
        print(f"There is a {room.item.name} here.")
    names = []
    for r in room.exits:
        names.append(r.name)
    print("Exits: " + ", ".join(names))


def move_player(player):
    exits = player.location.exits
    for i in range(len(exits)):
        print(f"{i + 1}. {exits[i].name}")
    choice = input("Where do you want to go? ")
    if choice.isdigit() and 1 <= int(choice) <= len(exits):
        player.move(exits[int(choice) - 1])
        print(f"You went to the {player.location.name}.")
        print(player.location.description)
    else:
        print("You stay where you are.")


def take_item(player):
    item = player.collect_item()
    if item is None:
        print("There is nothing to pick up here.")
    else:
        print(f"You picked up the {item.name}.")


def show_inventory(player):
    if len(player.items) == 0:
        print("Your backpack is empty.")
    else:
        print("Your backpack has:")
        for item in player.items:
            print(f"{item.name} ({item.weight} kg)")
        print(f"Total weight: {player.total_weight():.2f} kg")


def rest(player):
    print(f"{player.name} sits down in the {player.location.name} and takes a break.")
