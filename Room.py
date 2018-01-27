import random
import Item

class Room:
    descriptions = ["big, with massive paintings hung on the wall", "cramped, with barely any space to move at all", "smelly, like old oatmeal"]
    def __init__(self, roomdescription, items):
        self.description = roomdescription
        self.items = []
        for i in items:
            self.items.append(Item.Item(i))
        
    def StartRoom(self):
        self.description = "Welcome to the ship"
        self.items = [Item.Item()]
    
    def RandomRoom(self):
        self.description = random.choice(Room.descriptions)
        self.items = [Item.Item("test").RandomItem()]
        return self
        
