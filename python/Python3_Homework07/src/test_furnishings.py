'''
Created on Apr 23, 2014

@author: jgarza
'''
import unittest
from furnishings import *

class Test(unittest.TestCase):


    def test_append(self):
        """ Test the addition of a furnishing to home
            and check the attributes
        """
        home = []
        home.append(Bed('Bedroom'))
        self.assertEqual(home[0].room, 'Bedroom')
        self.assertEqual(home[0].name, 'Bed')
        
    def test_map_the_home(self):
        """ Test the number of objects added to home, then
            test to see if the number of room groups is correct
            after calling map_the_home
        """
        home = []
        home.append(Bed('Bedroom'))
        home.append(Sofa('Living Room'))
        home.append(Table('Living Room'))
        self.assertEqual(len(home),3)
        self.assertEqual(len(map_the_home(home)), 2)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()