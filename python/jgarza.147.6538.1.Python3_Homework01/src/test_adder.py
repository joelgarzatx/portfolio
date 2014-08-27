'''
Created on Apr 1, 2014

@author: jgarza
Test the adder() function from the adder module
'''
import unittest
from adder import adder

class Test(unittest.TestCase):

    def testadder_non_numeric(self):
        self.assertRaises(TypeError, adder, ('a',1))
        self.assertRaises(TypeError, adder, (1,'b'))

    def testadder_non_integer(self):
        self.assertRaises(TypeError, adder, (1.5, 1))
        self.assertRaises(TypeError, adder, (1,1.5))
        self.assertRaises(TypeError, adder, ('2', '3'))
        self.assertRaises(TypeError, adder, (1.0, 2.0))
        
    def testadder_result(self):
        self.assertEqual(adder(3,5), 8, "Result not as expected")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testadder']
    unittest.main()