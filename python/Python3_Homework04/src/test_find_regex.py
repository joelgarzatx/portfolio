'''
Created on Apr 5, 2014

@author: jgarza
Test module for find_regex.py
'''
import unittest
from find_regex import find_regex

class Test(unittest.TestCase):

    def setUp(self):
        self.target_string = """
In the 1950s, mathematician Stephen Cole Kleene described automata theory and formal language theory in a set of models using a notation called "regular sets" as a method to do pattern matching. Activeusage of this system, called Regular Expressions, started in the 1960s and continued under such pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry Spencer.                
        """
        self.pattern_string = "Regular Expressions"
        self.bad_pattern_string = "RRegular Expressions"
        
    def test_find_regex(self):
        self.assertEqual((231,250), find_regex(self.target_string, self.pattern_string))
        
    def test_not_find_regex(self):
        self.assertIsNone(find_regex(self.target_string, self.bad_pattern_string))



if __name__ == "__main__":
    unittest.main()