# Room class
# A room is one place in the forest. It can contain one item, it can need an item
# before the player is allowed in, and it can have a nature task (the SDG part of the game).


class Room:
    def __init__(self, name, item=None, description="", required_item=None):
        self.name = name
        self.item = item
        self.description = description
        self.required_item = required_item  # name of the item needed to enter, or None
        self.exits = []                     # rooms the player can move to from here
        self.task = None                    # a problem in nature that the player can fix
        self.task_done_text = ""            # text that is shown when the problem is fixed
        self.task_done = False

    def connect(self, other_room):
        # connects two rooms both ways
        self.exits.append(other_room)
        other_room.exits.append(self)

    def add_task(self, task, task_done_text):
        self.task = task
        self.task_done_text = task_done_text

    def has_open_task(self):
        # returns True if there is a nature task here that has not been done yet
        return self.task is not None and not self.task_done
