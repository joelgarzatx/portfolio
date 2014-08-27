'''
test_decoder.py: Tests module decoder.py

@author: jgarza
'''
from string import ascii_uppercase
import unittest
from decoder import alphabator

class TestAlpha(unittest.TestCase):

    def test_easy_26(self):
        """ Confirm list of integers 1-26 generates 26-letter alphabet (upper case) """
        a = alphabator(range(1,27))
        self.assertEqual(list(ascii_uppercase), list(a))

    def test_upper_range(self):
        """ Confirm list of integers outside of range for letters returns same list of integers """
        a = alphabator(range(40,50))          
        self.assertEqual(list(range(40, 50)), list(a))

    def test_various_objects(self):
        """ Confirm alphabator returns items as expected, including non-integer objects """
        l = ['python', object, ascii_uppercase, 10, alphabator]
        a = list(alphabator(l))
        self.assertNotEqual(l[3], a[3])
        self.assertEqual("J", a[3])
        self.assertTrue(isinstance(a[1], object))
    
    def test_is_iterable(self):
        """ Confirm the generator function is an iterable """
        self.assertTrue("__next()__ is in dir(alphabator)")
        self.assertTrue("__iter()__ is in dir(alphabator)")

if __name__ == "__main__":
    unittest.main()
