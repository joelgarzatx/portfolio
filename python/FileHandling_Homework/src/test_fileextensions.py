import os
import unittest
import tempfile
import fileextensions
import shutil

class TestFileextensions(unittest.TestCase):
    
    def setUp(self):
        self.file_names = []
        self.numtxtfiles = 5
        self.numpyfiles = 3
        
        for i in range(self.numtxtfiles):
            self.file_names.append('textfile' + str(i)+'.txt')
        for i in range(self.numpyfiles):
            self.file_names.append('pyfile' + str(i) + '.py')
        
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
        
        for filename in self.file_names:
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
 
    def test_1(self):
        "Verify that the counts are the same"
        expected = [('.txt',self.numtxtfiles),('.py',self.numpyfiles)]
        self.assertEqual(set(fileextensions.print_file_ext_count(self.dirname)),set(expected), "Counts are not the same")

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)          

if __name__ == "__main__":
    unittest.main()