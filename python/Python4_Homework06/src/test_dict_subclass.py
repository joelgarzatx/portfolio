'''
Test module for dict_subclass.py

Created on Apr 30, 2014

@author: jgarza
'''
import unittest
from dict_subclass import *

class Test(unittest.TestCase):

    def test_Dict(self):
        # create an object instance of class Dict passing a default value
        # validate dictionary is empty, add to key,value pair, check length
        # attempt to access a valid key, attempt to access an invalid key
        self.d = Dict("default_value")
        self.assertEqual(self.d,{})
        self.d["a"] = "some value"
        self.d["b"] = "another value"
        self.assertEqual(len(self.d),2)
        self.assertEqual(self.d["a"], "some value")
        self.assertEqual(self.d["c"], "default_value")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_suite']
    unittest.main()