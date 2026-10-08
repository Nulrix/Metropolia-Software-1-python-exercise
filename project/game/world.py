# Game world
# Creates the items and rooms, connects the rooms and adds the nature tasks.
# There are three different routes from the forest path to the ranger station,
# and each route needs a different item (old map, lantern or rope).

from game.item import Item
from game.room import Room


def create_world():
    # the three items that open the three routes
    lantern = Item("lantern", 1.5)
    rope = Item("rope", 2.0)
    old_map = Item("old map", 0.1)

    forest_path = Room("forest path", None, "A narrow path in the middle of the dark forest. The sun is going down.")
    cabin = Room("old cabin", lantern, "An empty wooden cabin. Nobody has lived here for years.")
    cave = Room("dark cave", rope, "The entrance of a cave. Cold air is coming from inside.")
    river = Room("river bank", old_map, "A fast river runs through the forest.")

    # the trails can only be entered with the right item
    hidden_trail = Room("hidden trail", None, "A small trail that is only marked on the old map.", "old map")
    cave_tunnel = Room("cave tunnel", None, "A long tunnel through the hill. It is completely dark.", "lantern")
    waterfall = Room("waterfall cliff", None, "A steep cliff next to a waterfall. You climb down with the rope.", "rope")
    station = Room("ranger station", None, "The ranger station! The lights are on and someone is waiting.")

    # the map: forest path is in the middle, every trail leads to the ranger station
    forest_path.connect(cabin)
    forest_path.connect(cave)
    forest_path.connect(river)
    cabin.connect(hidden_trail)
    cave.connect(cave_tunnel)
    river.connect(waterfall)
    hidden_trail.connect(station)
    cave_tunnel.connect(station)
    waterfall.connect(station)

    # nature tasks (SDG 15: Life on Land)
    forest_path.add_task("Plastic bottles and snack wrappers are lying on the ground.",
                         "You collect the trash so that animals don't eat it.")
    cabin.add_task("A campfire next to the cabin is still smoking.",
                   "You put out the campfire with water from the well. You stopped a forest fire!")
    cave.add_task("Someone left a leaking oil can next to a small stream.",
                  "You close the can and carry it away from the water.")
    river.add_task("A small fox is stuck in an old fishing net.",
                   "You carefully untangle the net and the fox runs back into the forest.")
    hidden_trail.add_task("A young tree has fallen over and its roots are in the air.",
                          "You stand the tree back up and press the soil around its roots.")
    cave_tunnel.add_task("Bats are sleeping on the ceiling and your lantern is very bright.",
                         "You turn the lantern down and walk quietly so the bats can keep sleeping.")
    waterfall.add_task("Old car tyres have been dumped into the water.",
                       "You pull the tyres out of the water so the ranger can take them away.")

    return [forest_path, cabin, cave, river, hidden_trail, cave_tunnel, waterfall, station]


def find_room(rooms, name):
    # returns the room with this name, or None if there is no such room
    for room in rooms:
        if room.name == name:
            return room
    return None
