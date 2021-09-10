class Room:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.songs = []
        self.guests = []

    # def check_in_guest(self, guest):
    #     self.guests.append(guest)

    # Extension..

    def check_in_guest(self, guest):
        if len(self.guests) == self.capacity:
            return "Sorry this room is full"
        else:
            self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)
