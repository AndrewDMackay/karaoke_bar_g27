import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Wine", 5.00)
        
    # Test a drink has a name..

    def test_drink_has_a_name(self):
        self.assertEqual("Wine", self.drink.name)
     
    # Test a drink has a price..
       
    def test_drink_has_a_price(self):
        self.assertEqual(5.00, self.drink.price) 
                 
