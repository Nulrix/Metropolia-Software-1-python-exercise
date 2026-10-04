class Player:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.items = []
        self.location = location

    def move(self, destination):
        self.location = destination

    def collect_item(self):
        item = self.location.item
        if item is not None:
            self.items.append(item)
            self.location.item = None
        return item

    def total_weight(self):
        total = 0
        for item in self.items:
            total += item.weight
        return total
