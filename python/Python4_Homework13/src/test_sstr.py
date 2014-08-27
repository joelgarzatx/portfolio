'''
Created on May 2, 2014
test_sstr.py : tests module sstr.py
@author: jgarza
'''
import unittest
from sstr import *


class Test(unittest.TestCase):


    def test_shift(self):
        s = sstr("abcde")
        self.assertEqual(s << 0, "abcde")
        self.assertEqual(s >> 0, "abcde")
        self.assertEqual(s << 2, "cdeab")
        self.assertEqual(s >> 2, "deabc")
        self.assertEqual(s >> 5, "abcde")
        self.assertTrue((s >> 5) << 5 ==  "abcde")
        self.assertRaises(TypeError, s >> 2.3)
        self.assertTrue(s >> -1 == s << 1) # Supports negative shift as reverse direction

        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_shift']
    unittest.main()