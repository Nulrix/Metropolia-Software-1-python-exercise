# Dark Forest Adventure

TaeQ Yoon

A text adventure game played in the command line, made for the Metropolia Software 1 course.

## Story and objective

The player went hiking but walked too far from the marked path. The sun is going down, the phone has no signal and the player is lost in a dark forest.

**Objective:** find the way to the ranger station. On the way the player sees problems that people have caused in the forest (trash, a smoking campfire, an animal stuck in a fishing net...). The player can fix them, and the ending depends on how much they helped.

## Sustainable development goal

The game is built around **UN SDG 15: Life on Land** (protect forests and wildlife). Every place in the forest has a nature problem. With the `eco` command the player fixes it and gets an eco point:

- picking up plastic trash so animals don't eat it
- putting out a campfire to prevent a forest fire
- freeing a fox from an old fishing net
- moving a leaking oil can and old tyres away from the water
- replanting a fallen young tree and not disturbing sleeping bats

The number of eco points decides which of the three endings the player gets, so helping nature is part of winning the game.

## How to run

Run `main.py` from the `project` folder:

```
python main.py
```

The game is for players aged 12 and over. Younger players are told they are minors and the game closes.

## How to play

The game starts with a start menu: new game, continue a saved game, show results or quit. After that the main menu commands are:

| Command | What it does |
|---|---|
| `look` | shows the place, its item, its nature problem and where you can go |
| `move` | moves to a connected place (chosen with a number) |
| `collect` | picks up the item in the current place |
| `eco` | fixes the nature problem in the current place (+1 eco point) |
| `inventory` | shows the items, their total weight and the eco points |
| `map` | shows the map of the forest (only if you carry the old map) |
| `save` | saves the game |
| `help` | shows the instructions |
| `lopeta` | quits the game (asks if you want to save first) |

## Routes

The game starts at the forest path. The old cabin, the dark cave and the river bank are next to it. Each of them leads to a trail that needs an item, and every trail ends at the ranger station:

1. **Map route:** get the old map at the river bank, go through the old cabin to the hidden trail
2. **Cave route:** get the lantern in the old cabin, go through the dark cave to the cave tunnel
3. **River route:** get the rope in the dark cave, go through the river bank to the waterfall cliff

## Endings

- **Forest Guardian:** 5 or more eco points
- **Friend of the Forest:** 3-4 eco points
- **Safe but Worried:** 0-2 eco points

## How the program works

- `main.py` has the start menu loop and the main menu loop. Each command is its own function.
- The game world is made of objects: `Room` objects are connected to each other with `connect()`, some rooms have an `Item`, and the `Player` object knows its location, its items and where it has helped nature.
- A room can have `required_item`. Before moving, `Player.can_enter()` checks that the player carries that item. This is how the three routes work.
- When the player reaches the ranger station, the result is written to `results.txt` and the save file is deleted.

## Files

```
project/
├── main.py                  final game, run this file
├── readme.md
├── intro.txt                story shown when the game starts
├── instructions.txt         instructions (shown at start and with 'help')
├── map.txt                  map shown with the 'map' command
├── game/                    package for the game code
│   ├── __init__.py
│   ├── item.py              Item class (name, weight)
│   ├── room.py              Room class (name, item, description, required item, exits, nature task)
│   ├── player.py            Player class (name, age, items, location, helped rooms, moves)
│   ├── world.py             create_world() builds the map, find_room() finds a room by name
│   └── file_handling.py     reading text files, saving/loading, results
└── module_*_project_*.py    the earlier project subtasks (projects 1-5)
```

Files created while playing:

- `save_<name>.txt` - the saved game of a player (location, items, done nature tasks, moves)
- `results.txt` - one line for each finished game, shown in the start menu

## Own features

- three different endings based on eco points
- results table of all finished games, saved in a file
- the old map item can be read with the `map` command
- locked trails that need the right item
- move counter
