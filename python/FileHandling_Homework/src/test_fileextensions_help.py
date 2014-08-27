import os
import unittest
import tempfile
import shutil

class TestFileextensions(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
        
        # Peek at self.dirname
        print("setUp: " + self.dirname)
 
    def test_1(self):
        "Verify that the current directory is empty"
        # Peek at self.dirname
        print("test_1: " + self.dirname)
                 
    def test_2(self):
        "Verify creation of files is possible"
        # Peek at self.dirname
        print("test_2: " + self.dirname)
    
    def test_3(self):
        "Verify that the counts are the same"
        # Peek at self.dirname
        print("test_3: " + self.dirname)

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
        # Peek at self.dirname
        print("tearDown: " + self.dirname)          

if __name__ == "__main__":
    unittest.main()