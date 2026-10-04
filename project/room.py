class Room:
    def __init__(self, name, description, item=None):
        self.name = name
        self.description = description
        self.item = item
        self.exits = []

    def connect(self, other_room):
        self.exits.append(other_room)
        other_room.exits.append(self)
