'''
Created on May 1, 2014
Test suite for addarg_decorator
@author: jgarza
'''
import unittest
from addarg_decorator import *

class Test(unittest.TestCase):
          
    def test_addarg(self):
        self.assertTupleEqual(prargs(2,3),(1, 2, 3))
        self.assertTupleEqual(prargsnkwargs(2,3), ((10, 2, 3),{}))
        self.assertTupleEqual(prargsnkwargs(4,5,6,name='bob',job='foreman'),((10, 4, 5, 6), {'name':'bob', 'job': 'foreman'}))
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_addarg']
    unittest.main()