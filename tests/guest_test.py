import unittest

from src.venue import Venue
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Steve", 100, "Lady In Red")
        self.venue = Venue("Steve's Karaoke", 1000, 10)
        self.song = Song("Lady In Red", "Chris De Burgh")
        self.songs = ["Lady In Red", "Don't Pay The Ferryman", "Missing You"]

# Test a guest has name..

    def test_guest_has_name(self):
        self.assertEqual("Steve", self.guest1.name)

# Test a guest has wallet..

    def test_guest_has_wallet(self):
        self.assertEqual(100, self.guest1.wallet)

# Extensions.. 

# Test guest wallet decreased by entry fee..

    def test_guest_wallet_decreased_by_entry_fee(self):
        self.guest1.remove_entry_fee(self.venue.entry_fee)
        self.assertEqual(90, self.guest1.wallet)
        
# Advanced extension 1..

# Test a guest has favourite song..

    def test_guest_has_favourite_song(self):
        self.assertEqual("Lady In Red", self.guest1.favourite_song)

# Test a guest cheers for their favourite song..

    def test_guest_cheers_for_their_favourite_song(self):
        self.assertEqual("Woo hoo!", self.guest1.cheer_for_favourite_song(self.songs))
