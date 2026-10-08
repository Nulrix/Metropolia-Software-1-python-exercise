# Dark Forest Adventure - final version
# Start menu, main menu loop and the functions for the game commands.

from game.world import create_world
from game.player import Player
from game.file_handling import read_text_file, save_exists, save_game, load_game
from game.file_handling import delete_save, save_result, read_results


def show_start_menu():
    print("\n=== DARK FOREST ADVENTURE ===")
    print("1 - new game")
    print("2 - continue a saved game")
    print("3 - show results")
    print("4 - quit")


def show_menu():
    print("\n=== MAIN MENU ===")
    print("look - look around")
    print("move - move to another place")
    print("collect - collect the item here")
    print("eco - help nature in this place")
    print("inventory - show your items and eco points")
    print("map - read the old map")
    print("save - save the game")
    print("help - show the instructions")
    print("lopeta - quit the game")


def ask_name():
    name = input("Enter your name: ").strip()
    while name == "":
        name = input("The name can't be empty. Enter your name: ").strip()
    return name


def ask_age():
    age = input("Enter your age: ")
    while not age.isdigit():
        age = input("Enter your age as a number: ")
    return int(age)


def new_game(rooms):
    # returns a new Player, or None if the player is too young to play
    name = ask_name()
    age = ask_age()
    if age < 12:
        print("You are a minor. This game is for players aged 12 and over. The game will now close.")
        return None

    print(f"\nWelcome, {name}!")
    print(f"You are {age} years old.")
    print("Your adventure begins now...\n")
    print(read_text_file("instructions.txt"))
    return Player(name, age, rooms[0])


def continue_game(rooms):
    # returns the saved Player, or None if there is no save for this name
    name = ask_name()
    if not save_exists(name):
        print(f"No saved game was found for {name}.")
        return None
    player = load_game(name, rooms)
    print(f"\nWelcome back, {player.name}!")
    return player


def show_results():
    results = read_results()
    if len(results) == 0:
        print("Nobody has finished the game yet.")
        return
    print("\nFINISHED GAMES")
    print(f"{'Name':<12}{'Route':<18}{'Eco points':<12}{'Moves':<6}")
    for result in results:
        print(f"{result[0]:<12}{result[1]:<18}{result[2]:<12}{result[3]:<6}")


def look(player):
    room = player.location
    print(f"\n--- {room.name.upper()} ---")
    print(room.description)
    if room.item is not None:
        print(f"You see an item here: {room.item.name}")
    if room.has_open_task():
        print(f"Nature needs help: {room.task} (use 'eco')")

    exit_names = []
    for next_room in room.exits:
        exit_names.append(next_room.name)
    print("From here you can go to: " + ", ".join(exit_names))


def move_player(player):
    # moves the player to the place they choose
    # returns True if the player reached the ranger station, so the game can end
    exits = player.location.exits
    print("Where do you want to go?")
    for i in range(len(exits)):
        print(f"{i + 1}. {exits[i].name}")
    choice = input("Enter a number: ")

    if not choice.isdigit() or not 1 <= int(choice) <= len(exits):
        print("There is no such place.")
        return False

    destination = exits[int(choice) - 1]
    if not player.can_enter(destination):
        print(f"You can't go to the {destination.name} yet. You need: {destination.required_item}")
        return False

    previous_room = player.location
    player.move(destination)
    if destination.name == "ranger station":
        finish_game(player, previous_room.name)
        return True
    look(player)
    return False


def show_inventory(player):
    if len(player.items) == 0:
        print("Your backpack is empty.")
    else:
        print("Your backpack:")
        for item in player.items:
            print(f"- {item.name} ({item.weight} kg)")
        print(f"Total weight: {player.total_weight():.1f} kg")
    print(f"Eco points: {player.eco_points()}")


def do_eco_task(player):
    room = player.location
    if player.help_nature():
        print(f"{room.task_done_text} (+1 eco point)")
    else:
        print("There is nothing to fix here right now.")


def show_map(player):
    # the map can only be read if the player carries the old map
    if player.has_item("old map"):
        print(read_text_file("map.txt"))
    else:
        print("You don't have a map. Maybe you can find one somewhere...")


def get_ending(points):
    # returns the ending text, the ending depends on how much the player helped nature
    if points >= 5:
        return ("ENDING: FOREST GUARDIAN\n"
                "The ranger has already heard about everything you did today.\n"
                "She gives you a Forest Guardian badge and asks you to come back as a volunteer.")
    elif points >= 3:
        return ("ENDING: FRIEND OF THE FOREST\n"
                "The ranger thanks you for helping. Together you plan how to clean up the rest of the forest.")
    else:
        return ("ENDING: SAFE BUT WORRIED\n"
                "You made it out safely. On the way home you think about the trash and the animals\n"
                "you saw, and you decide to come back and help next time.")


def finish_game(player, route):
    points = player.eco_points()
    print(f"\nYou came through the {route} and reached the ranger station!")
    print(get_ending(points))
    print(f"\nEco points: {points}   Moves: {player.moves}")
    save_result(player, route)
    delete_save(player.name)


# ----- main program -----

print(read_text_file("intro.txt"))

rooms = create_world()
player = None

# start menu: runs until a game is started or the player quits
choice = ""
while player is None and choice != "4":
    show_start_menu()
    choice = input("Choose: ").strip()
    if choice == "1":
        player = new_game(rooms)
        if player is None:
            choice = "4"  # minors can't play, so the game closes
    elif choice == "2":
        player = continue_game(rooms)
    elif choice == "3":
        show_results()
    elif choice != "4":
        print("Choose 1, 2, 3 or 4.")

# main menu: runs until the player quits or reaches the ranger station
if player is not None:
    look(player)
    game_finished = False
    command = ""
    while command != "lopeta" and not game_finished:
        show_menu()
        command = input("Enter command: ").strip().lower()

        if command == "look":
            look(player)
        elif command == "move":
            game_finished = move_player(player)
        elif command == "collect":
            player.collect_item()
        elif command == "eco":
            do_eco_task(player)
        elif command == "inventory":
            show_inventory(player)
        elif command == "map":
            show_map(player)
        elif command == "save":
            save_game(player)
            print("The game was saved. Choose 'continue' and enter the same name next time.")
        elif command == "help":
            print(read_text_file("instructions.txt"))
        elif command == "lopeta":
            answer = input("Do you want to save before quitting? (y/n): ").lower()
            if answer == "y":
                save_game(player)
                print("The game was saved.")
        else:
            print("Unknown command. Type 'help' to see the instructions.")

    print(f"\nThanks for playing, {player.name}!")
