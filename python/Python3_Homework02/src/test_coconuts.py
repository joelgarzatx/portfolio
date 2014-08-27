'''
Created on Apr 2, 2014
@author: jgarza

Test the coconuts module
'''
import unittest
from coconuts import Coconut
from coconuts import Inventory

class Test_coconuts(unittest.TestCase):
    def setUp(self):
        self.c1 = Coconut("American")
        self.c2 = Coconut("Middle Eastern")
        self.c3 = Coconut("South Asian")   
             
    def test_coconut_bad(self):
        self.assertRaises(KeyError, Coconut, "West European")
        
    def test_coconut_attributes(self):    
        self.assertEqual("American", self.c1.coconut_type)
        self.assertEqual(3.5, self.c1.coconut_weight)
        self.assertEqual("Middle Eastern", self.c2.coconut_type)
        self.assertEqual(2.5, self.c2.coconut_weight)
        self.assertEqual("South Asian", self.c3.coconut_type)
        self.assertEqual(3, self.c3.coconut_weight)
        
    def test_inventory_bad(self):
        i = Inventory()
        self.assertRaises(AttributeError, i.add_coconut, "American")
    
    def test_inventory_total_weight(self):
        i = Inventory()
        for count in range(3):
            i.add_coconut(self.c1)
        for count in range(1):
            i.add_coconut(self.c2)
        for count in range(2):
            i.add_coconut(self.c3)
        self.assertEqual(19, i.total_weight(), "Calculated weight not correct")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_coconuts']
    unittest.main()