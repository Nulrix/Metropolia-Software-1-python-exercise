# File handling
# Reads the text files (intro, instructions, map), saves and loads the game,
# and keeps a list of finished games in results.txt.

import os

from game.player import Player
from game.world import find_room

RESULTS_FILE = "results.txt"


def read_text_file(filename):
    # returns the text of the file, or a short message if the file is missing
    if not os.path.exists(filename):
        return f"({filename} was not found)"
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def save_file_name(player_name):
    # every player has their own save file, for example save_taeq.txt
    return f"save_{player_name.lower()}.txt"


def save_exists(player_name):
    return os.path.exists(save_file_name(player_name))


def save_game(player):
    # writes the game state into the save file, one value per line
    item_names = []
    for item in player.items:
        item_names.append(item.name)

    with open(save_file_name(player.name), "w", encoding="utf-8") as file:
        file.write(player.name + "\n")
        file.write(str(player.age) + "\n")
        file.write(player.location.name + "\n")
        file.write(",".join(item_names) + "\n")
        file.write(",".join(player.helped_rooms) + "\n")
        file.write(str(player.moves) + "\n")


def load_game(player_name, rooms):
    # reads the save file and returns a Player that continues from the saved state
    with open(save_file_name(player_name), "r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    location = find_room(rooms, lines[2])
    if location is None:
        location = rooms[0]
    player = Player(lines[0], int(lines[1]), location)

    # the saved items are taken out of the rooms and given back to the player
    for item_name in lines[3].split(","):
        for room in rooms:
            if room.item is not None and room.item.name == item_name:
                player.items.append(room.item)
                room.item = None

    # nature tasks that were already done stay done
    for room_name in lines[4].split(","):
        room = find_room(rooms, room_name)
        if room is not None:
            room.task_done = True
            player.helped_rooms.append(room_name)

    if len(lines) > 5:
        player.moves = int(lines[5])
    return player


def delete_save(player_name):
    # removes the save file when the game has been finished
    if save_exists(player_name):
        os.remove(save_file_name(player_name))


def save_result(player, route):
    # adds one line to the results file ("a" = append, old results are kept)
    with open(RESULTS_FILE, "a", encoding="utf-8") as file:
        file.write(f"{player.name};{route};{player.eco_points()};{player.moves}\n")


def read_results():
    # returns a list of results, each result is a list: [name, route, eco points, moves]
    results = []
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(";")
                if len(parts) == 4:
                    results.append(parts)
    return results
