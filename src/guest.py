
class Guest:
    
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def remove_entry_fee(self, entry_fee):
        self.wallet -= entry_fee

         # Advanced Extensions..

    def cheer_for_favourite_song(self, songs):
        for song in songs:
            if song == self.favourite_song:
                return "Woo hoo!"
            else:
                pass