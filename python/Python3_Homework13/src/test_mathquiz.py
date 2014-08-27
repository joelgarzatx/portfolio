'''
Created on Apr 27, 2014

@author: jgarza
'''

import unittest
from mathquiz import *


class Test(unittest.TestCase):


    def setUp(self):
        self.rand_num_1 = randint(1,10)
        self.rand_num_2 = randint(1,10)
        self.num_sum = self.rand_num_1 + self.rand_num_2        
        
    def test_quiz_sum(self):
        self.assertEqual(quiz_sum(self.rand_num_1, self.rand_num_2),self.num_sum,"Calculated sums not equal")
        
    def test_question(self):
        question = Question(self.rand_num_1, self.rand_num_2)
        self.assertEqual(question.num_1, self.rand_num_1, "Object value not equal")
        self.assertEqual(question.num_2, self.rand_num_2, "Object value not equal")
        self.assertEqual(question.num_sum, self.num_sum, "Calculated sums not equal")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_quiz']
    unittest.main()