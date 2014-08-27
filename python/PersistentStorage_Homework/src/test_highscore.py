import unittest
import highscore
import shelve
import glob
import os


class TestHighscore(unittest.TestCase):

    def setUp(self):
        self.head = r'v:\workspace\PersistentStorage_Homework\src'
        self.tail = 'myshelf.shlf'
        shelf = shelve.open(os.path.join(self.head, self.tail))
        # Alice does not have a previous score
        shelf['Bob'] = 10
        shelf['Carol'] = 12
        shelf.close()
 
    def test_1(self):
        "Player with no previous score"
        self.assertEqual(highscore.check_player_score("Alice",12),12)
        
    def test_2(self):
        "Player with current score equal or lower"
        self.assertEqual(highscore.check_player_score("Bob",10),10)
        self.assertEqual(highscore.check_player_score("Bob",8),10)

    def test_3(self):
        "Player with current score higher"
        self.assertEqual(highscore.check_player_score("Carol",14),14)
        pass

    def tearDown(self):
        filelist = glob.glob(os.path.join(self.head, 'myshelf.*'))
        for file in filelist:
            os.remove(os.path.join(self.head, file))

if __name__ == "__main__":
    unittest.main()