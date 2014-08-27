'''
Created on Apr 23, 2014

@author: jgarza
'''
import unittest
from ccn_safety import ccn_hide

text = """Have you ever noticed, in television and movies, that phone numbers and credit cards
are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number
that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and security experts.
"""
class TestRegex(unittest.TestCase):


    def test_ccn(self):
        response, count = ccn_hide(text)
        self.assertFalse("5555-5555-5555-5555" in response)
        self.assertTrue("XXXX-XXXX-XXXX-5555" in response)
        self.assertTrue("XXXX-XXXX-XXXX-5678" in response)
        self.assertTrue("555-123-4567" in response)
        self.assertEqual(2, count)


if __name__ == "__main__":
    unittest.main()