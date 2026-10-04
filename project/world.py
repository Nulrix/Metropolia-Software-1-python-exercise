from game.item import Item
from game.room import Room


def create_world():
    flashlight = Item("flashlight", 0.4)
    usb = Item("USB stick", 0.02)
    keycard = Item("keycard", 0.01)

    lobby = Room("Lobby", "A dark entrance hall. The main door is locked.")
    office = Room("Office", "Desks full of coffee cups and old papers.", usb)
    storage = Room("Storage room", "Shelves with old cables and broken keyboards.", flashlight)
    server_room = Room("Server room", "Servers are blinking and it's really cold.", keycard)

    lobby.connect(office)
    lobby.connect(storage)
    office.connect(server_room)

    return lobby
