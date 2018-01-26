import random

class Item:
    items = ["a Rake", "a Spoon", "a Flashlight", "a Key", "a Gun"]
    def __init__(self):
        self.name = random.choice(Item.items)
