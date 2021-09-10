import unittest

from src.guest import Guest
from src.venue import Venue

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Steve", 100, "Lady In Red")
        self.venue = Venue("Steve's Karaoke", 1000, 10)

# Test a guest has name..

    def test_guest_has_name(self):
        self.assertEqual("Steve", self.guest.name)

# Test a guest has wallet..

    def test_guest_has_wallet(self):
        self.assertEqual(100, self.guest.wallet)

# Extension.. 

# Test guest wallet decreased by entry fee..

    def test_guest_wallet_decreased_by_entry_fee(self):
        self.guest.remove_entry_fee(self.venue.entry_fee)
        self.assertEqual(90, self.guest.wallet)
        
# Advanced extensions..

# Test a guest has favourite song..

    def test_guest_has_favourite_song(self):
        self.assertEqual("Lady In Red", self.guest.favourite_song)
