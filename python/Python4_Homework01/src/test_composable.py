'''
Created on Apr 27, 2014
test_composable.py performs simple tests of composable functions.
@author: jgarza
'''
import unittest
from composable import Composable

def reverse(s):
    "Reverses a string using negative-stride sequencing."
    return s[::-1]

def square(x):
    "Multiplies a number by itself"
    return x*x

def incrementer(x):
    "Adds a number to itself"
    return x + x

class ComposableTestCase(unittest.TestCase):

    def test_inverse(self):
        reverser = Composable(reverse)
        nulltran = reverser * reverser
        for s in "", "a", "0123456789", "abcdefghijklmnopqrstuvwxyz":
            self.assertEquals(nulltran(s), s)
            
    def test_square(self):
        squarer = Composable(square)
        po4 = squarer * squarer
        for v, r in ((1,1), (2,16), (3,81)):
            self.assertEqual(po4(v), r)
            
    def test_power_as_square(self):
        # should behave the same as the __mult__ with power of 2
        function_for_power = Composable(square)
        po4 = function_for_power ** 2
        for v, r in ((1,1), (2,16), (3,81)):
            self.assertEqual(po4(v), r)   
            
    def test_power_of_1_square(self):
        # power of 1 should just be the function
        function_for_power = Composable(square)
        po2 = function_for_power ** 1
        for v, r in ((1,1), (2,4), (3,9)):
            self.assertEqual(po2(v), r)  
            
    def test_power_of_1_doubler(self):
        # power of 1 should just be the function
        function_for_power = Composable(incrementer)
        po2 = function_for_power ** 1
        for v, r in ((1,2), (2,4), (3,6)):
            self.assertEqual(po2(v), r)  
                        
    def test_power(self):
        function_for_power = Composable(incrementer)
        po2 = function_for_power ** 3
        for v, r in ((1,8), (2,16), (3,24)):
            self.assertEqual(po2(v), r)  
            
    def test_mult_and_power(self):
        fc = Composable(square)
        func_a = fc ** 5
        func_b = fc * fc * fc * fc * fc
        val_a = func_a(2)
        val_b = func_b(2)
        self.assertEqual(val_a, val_b, "Mult and Power don't match {0} vs {1}.".format(val_a,val_b))
                    
    def test_exceptions(self):
        fc = Composable(square)
        with self.assertRaises(TypeError):
            fc = fc * 3
        with self.assertRaises(TypeError):
            fc = square * fc
        with self.assertRaises(TypeError):
            fc = fc ** 1.2
        with self.assertRaises(ValueError):
            fc = fc ** -4
            
if __name__ == "__main__":
    unittest.main()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_inverse']
    unittest.main()