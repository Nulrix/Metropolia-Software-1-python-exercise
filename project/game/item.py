# Item class
# An item has a name and a weight. Items lie in rooms and the player can collect them.


class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
