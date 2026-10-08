# Player class
# The player has a name, an age, a list of items and a location (the room the player is in).
# The player also remembers where they helped nature and how many moves they have made.


class Player:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.items = []
        self.location = location
        self.helped_rooms = []  # names of the rooms where the player did the nature task
        self.moves = 0

    def move(self, destination):
        self.location = destination
        self.moves += 1
        print(f"You moved to the {destination.name}.")

    def collect_item(self):
        # moves the item from the current room to the player's items
        # returns the item, or None if there was nothing to collect
        item = self.location.item
        if item is None:
            print("There is nothing to collect here.")
        else:
            self.items.append(item)
            self.location.item = None
            print(f"You collected the {item.name} ({item.weight} kg).")
        return item

    def has_item(self, item_name):
        # returns True if the player carries an item with this name
        for item in self.items:
            if item.name == item_name:
                return True
        return False

    def can_enter(self, room):
        # returns True if the room needs no item, or if the player has the needed item
        if room.required_item is None:
            return True
        return self.has_item(room.required_item)

    def help_nature(self):
        # does the nature task in the current room
        # returns True if the player helped, False if there was nothing to do
        room = self.location
        if not room.has_open_task():
            return False
        room.task_done = True
        self.helped_rooms.append(room.name)
        return True

    def eco_points(self):
        # one eco point for every place where the player helped nature
        return len(self.helped_rooms)

    def total_weight(self):
        total = 0
        for item in self.items:
            total += item.weight
        return total
