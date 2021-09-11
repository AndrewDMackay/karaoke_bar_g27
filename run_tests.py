import unittest
from tests.guest_test import TestGuest
from tests.room_test import TestRoom
from tests.song_test import TestSong
from tests.venue_test import TestVenue

if __name__ == '__main__':
    unittest.main()

# Homework..

# MVP..

# You have been approached to build software for a Karaoke bar. 
# Specifically, they want you to build a software for checking guests in and out, plus handling songs.

# Your program should be test driven and should be able to..

# Create rooms, songs and guests.
# Check in guests to rooms/Check out guests from rooms.
# Add songs to rooms.

# Extensions..

# What happens if there are more guests trying to be checked in than there is free space in the room?
# Karaoke venues usually have an entry fee - So the guests could have money so they can pay it.

# Advanced extensions..

# Guests could have a favourite song, and if their favourite song is on the room's playlist, they can cheer loudly! 
# (Return a string like "Whoo!")
# Rooms can keep track of the entry fees/spending of the guests - maybe add a bar tab/bar class?
# Add anything extra you think would be good to have at a karaoke venue!

