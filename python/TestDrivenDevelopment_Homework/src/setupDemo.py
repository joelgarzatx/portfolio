"""
Demonstration of setUp and tearDown.
The tests do not actually test anything - this is a demo.
"""
import unittest
import tempfile
import shutil
import glob
import os


class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")

        os.chdir(self.dirname)
    
    def test_1(self):
        "Verify creation of files is possible"
        temp_filenames = {"this.txt", "that.txt", "the_other.txt"}
        for filename in temp_filenames:
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
        # Test to see if there are any files in os.listdir that are not
        # in temp_filenames using the < operator for sets
        self.assertFalse(temp_filenames < set(os.listdir(self.dirname)))
            
    
    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")
        
    def test_3(self):
        """ Create and verify size of binary file to be one million bytes """
        f = open("file1milbyte",'wb')
        f.write(b'1' * 1000000)
        f.close()
        self.assertTrue(f.closed)
        statinfo = os.stat("file1milbyte")
        self.assertEqual(statinfo.st_size, 1000000, "Filesize not 1000000 bytes")
        

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
  

if __name__ == "__main__":
    unittest.main()

