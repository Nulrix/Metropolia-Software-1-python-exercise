# Room class
# A room has a name and can contain one item

class Room:
    def __init__(self, name, item=None):
        self.name = name
        self.item = item
