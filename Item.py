import random

class Item:
    items = ["a Rake", "a Spoon", "a Flashlight", "a Key", "a Gun"]
    def __init__(self, name):
        self.name = name

    def RandomItem(self):
        self.name = random.choice(Item.items)
        return self
