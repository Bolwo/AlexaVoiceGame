import Room
import Item
class Player:
    
    def __init__(self):
        self.inventory = "test"
        self.room = Room.Room()
        self.room.StartRoom()
        self.items = []
    
    def move(self):
        self.room = Room.Room()
        
    def pickup(self):
        for i in self.room.items:
            self.items.append(i)
        self.room.items = []
      
        
