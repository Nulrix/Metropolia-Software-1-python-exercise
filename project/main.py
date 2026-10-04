from game.player import Player
from game.world import create_world
from game import commands

player_name = input("Enter your name: ")
age = input("Enter your age: ")
while not age.isdigit():
    age = input("Enter your age as a number: ")
player_age = int(age)

if player_age < 12:
    print("You are a minor, so you can't play this game.")
else:
    start = create_world()
    player = Player(player_name, player_age, start)
    print(f"Hello {player.name}, welcome to Escape from the Server Room!")
    commands.look_around(player)

    command = ""
    while command != "lopeta":
        commands.show_menu()
        command = input("Enter command: ").strip().lower()
        if command == "look":
            commands.look_around(player)
        elif command == "move":
            commands.move_player(player)
        elif command == "take":
            commands.take_item(player)
        elif command == "inv":
            commands.show_inventory(player)
        elif command == "rest":
            commands.rest(player)
        elif command == "lopeta":
            print("Bye!")
        else:
            print("Unknown command.")
