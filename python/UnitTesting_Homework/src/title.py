"""
Python2 UnitTesting_Homework

Accepts a string of one or more words and capitalizes the first letter of each word.

"""
import unittest

def title(s):
    """ Returns same string with first character capitalized."""
    words = s.split()
    # Loop through the words and CAPS first letter
    for i,word in enumerate(words):
        words[i] = word[0].upper() + word[1:].lower()
    # Concatenate the words as string
    return " ".join(words)


class TestCube(unittest.TestCase):
    
    def test_all_lower(self):
        title_text = "this is an example."
        self.assertEqual(title(title_text), title_text.title(), "Title results should be same")
        
    def test_all_upper(self):
        title_text = "THIS IS ANOTHER EXAMPLE."
        self.assertEqual(title(title_text), title_text.title(), "Title results should be same")
        
    def test_already_title(self):
        title_text = "This is Another Example."
        self.assertEqual(title(title_text), title_text.title(), "Title results should be same")
        
if __name__ == "__main__":
    unittest.main()

