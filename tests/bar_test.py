import unittest

from src.bar import Bar
from src.guest import Guest
from src.drink import Drink


class TestBar(unittest.TestCase):

   def setUp(self):
      self.bar = Bar()
      self.drink1 = Drink("Wine", 5.00)
      self.drink2 = Drink("Beer", 3.00)
      self.drink3 = Drink("Soft", 2.50)
        
# Test the bar has a tab, that starts at 0..

   def test_bar_has_an_empty_tab(self):
      self.assertEqual(0.00, self.bar.tab)

# Test the bar can add a drink..

   def test_bar_can_add_drinks(self):
      self.bar.add_drink(self.drink1)
      self.assertEqual(1, len(self.bar.drinks))

# Test the bar tab increases after adding a drink, by the price of that drink..

   def test_bar_tab_increases_by_drink(self):
      self.bar.add_drink(self.drink1)
      self.bar.increase_tab_by_drink(self.drink1)
      self.assertEqual(5.00, self.bar.tab)

# Test the bar can print an itemised drinks tab..
   def test_bar_can_print_itemised_tab(self):
      self.bar.add_drink(self.drink1)
      self.bar.increase_tab_by_drink(self.drink1)
      self.assertEqual(5.00, self.bar.print_tab())
  
   
