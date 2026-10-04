# Escape from the Server Room

TaeQ Yoon

Text adventure game for the Software 1 course. You are stuck in a dark office building. You can move between rooms and collect items.

Run with `python main.py`

## Structure

- `main.py` - starts the game, asks name and age and runs the menu loop
- `game/` - package for the game code
  - `item.py` - Item class (name, weight)
  - `room.py` - Room class (name, description, item, exits)
  - `player.py` - Player class (name, age, items, location) with move and collect_item methods
  - `world.py` - creates the rooms and items and connects the rooms
  - `commands.py` - functions for the menu commands

## Map

Storage room - Lobby - Office - Server room

The game starts in the Lobby.

## Commands

look, move, take, inv, rest, lopeta
