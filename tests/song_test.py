import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Lady In Red", "Chris De Burgh")

# Test a song has a title..

    def test_song_has_title(self):
        self.assertEqual("Lady In Red", self.song.title)

# Test a song has an artist..

    def test_song_has_artist(self):
        self.assertEqual("Chris De Burgh", self.song.artist)

# # Test a song has a title, dictionary method..

#     def test_song_has_title(self):
#         self.assertEqual("Lady In Red", self.song.track["title"])

# # Test a song has an artist, dictionary method..

#     def test_song_has_artist(self):
#         self.assertEqual("Chris De Burgh", self.song.track["artist"])