import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Steve", 100)

# Test a guest has name..

    def test_guest_has_name(self):
        self.assertEqual("Steve", self.guest.name)

# Test a guest has wallet..

    def test_guest_has_wallet(self):
        self.assertEqual(100, self.guest.wallet)

# Extension.. 
# Test a guest has favourite song..

