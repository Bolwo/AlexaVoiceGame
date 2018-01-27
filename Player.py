import Room
import Item
class Player:
    
    def __init__(self, roomdescription, roomitems, playeritems):
        self.room = Room.Room(roomdescription, roomitems)
        self.items = []
        for i in playeritems:
            self.items.append(Item.Item(i))
    
    def move(self):
        self.room = self.room.RandomRoom()
        
    def pickup(self):
        for i in self.room.items:
            self.items.append(i)
        self.room.items = []
     
        
