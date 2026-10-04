# Player class
# A player has a name, age, a list of items and a location (the room the player is in)

class Player:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.items = []
        self.location = location

    def move(self, destination):
        self.location = destination
        print(f"You moved to the {destination.name}.")

    def collect_item(self):
        if self.location.item is None:
            print("There is nothing to collect here.")
        else:
            item = self.location.item
            self.items.append(item)
            self.location.item = None
            print(f"You collected the {item.name} ({item.weight} kg).")
