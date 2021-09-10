class Venue:
    
    def __init__(self, name, till):
        self.name = name
        self.rooms = []
        self.till = till
        
    def add_room(self, room):
        self.rooms.append(room)
