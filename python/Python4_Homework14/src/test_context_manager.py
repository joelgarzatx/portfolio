'''
Created on May 3, 2014

@author: jgarza
'''
import unittest
from context_manager import *

class Test(unittest.TestCase):


    def test_suppressed_error(self):
        """
        Attempt to verify the ValueError gets suppressed.
        Is there a better way to do this?
        """
        err = ValueError()
        self.assertTrue(err_raising_experience(err))
        
    def test_raised_error(self):
        """
        Tests that the supplied error instance gets
        raised to the surrounding context
        """
        err = TypeError("TypeError")
        self.assertRaises(TypeError, err_raising_experience,err)
        err = ZeroDivisionError("ZeroDivisionError")
        self.assertRaises(ZeroDivisionError, err_raising_experience,err)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_context_manager']
    unittest.main()