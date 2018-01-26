import random
import Item

class Room:
    descriptions = ["big, with massive paintings hung on the wall", "cramped, with barely any space to move at all", "smelly, like old oatmeal"]
    def __init__(self):
        self.description = random.choice(Room.descriptions) #make random
        self.items = [Item.Item()]
        
    def StartRoom(self):
        self.description = "Welcome to the ship"
        self.items = [Item.Item()]
