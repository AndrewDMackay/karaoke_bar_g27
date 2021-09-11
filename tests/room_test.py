import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(2)
        self.guest1 = Guest("Steve", 100, "Lady In Red")
        self.guest2 = Guest("Craig", 75, "Dont Pay The Ferryman")
        self.guest3 = Guest("Stan", 50, "Missing You")
        self.song = Song("Lady In Red", "Chris De Burgh")

# Test a room has capacity..
    
    def test_room_has_capacity(self):
        self.assertEqual(2, self.room.capacity)

# Test a room has songs..

    def test_room_has_songs(self):
        self.assertEqual([], self.room.songs)

# Test a room has guests..

    def test_room_has_guests(self):
        self.assertEqual([], self.room.guests)

# Test a room is empty..

    def test_room_is_empty(self):
        self.assertEqual([], self.room.songs)
        self.assertEqual([], self.room.guests)

# Test a guest can be checked into a room..

    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest1)
        self.assertEqual(1, len(self.room.guests))

# Test a guest can be checked out of a room..

    def test_check_out_guest(self):
        self.room.check_in_guest(self.guest1)
        self.room.check_out_guest(self.guest1)
        self.assertEqual(0, len(self.room.guests))

# Test a song can be added to a room..

    def test_add_song(self):
        self.room.add_song(self.song)
        self.assertEqual(1, len(self.room.songs))

# Alternative, via index..

    def test_add_song(self):
        self.room.add_song(self.song)
        self.assertEqual(self.song, self.room.songs[0])

# Extensions..

#  Test does a room stop checking in guests at capcity..

    def test_does_a_room_stop_checking_in_guests_at_capacity(self):
        self.room.check_in_guest(self.guest1)
        self.room.check_in_guest(self.guest2)
        self.room.check_in_guest(self.guest3)
        self.assertEqual(2, len(self.room.guests))

# Advanced extensions..

# Test does a guest cheer for their favourite song..

    # def test_guest_cheers_for_their_favourite_song(self):
    #     self.room.check_in_guest(self.guest1)
    #     self.room.add_song(self.song)
    #     self.guest.cheer_for_favourite_song(self.song)
    #     self.assertEqual()


