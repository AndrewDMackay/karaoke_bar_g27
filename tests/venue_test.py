import unittest

from src.venue import Venue
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestVenue(unittest.TestCase):
    def setUp(self):
        self.venue = Venue("Steve's Karaoke", 1000)
        self.room = Room(10)

# Test does a venue have a name..

    def test_venue_has_name(self):
        self.assertEqual("Steve's Karaoke", self.venue.name)

# Test does a venue have rooms..

    def test_venue_has_rooms(self):
        self.assertEqual([], self.venue.rooms)

# Test can you add a room to a venue..

    def test_can_add_room_to_venue(self):
        self.venue.add_room(self.room)
        self.assertEqual(1, len(self.venue.rooms))

# Extension..

# Test does a venue have a till..

    def test_venue_has_till(self):
        self.assertEqual(1000, self.venue.till)


