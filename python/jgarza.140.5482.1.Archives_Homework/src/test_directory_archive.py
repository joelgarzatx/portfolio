import unittest
import directory_archive as da
import os
import shutil
import zipfile

class TestZip(unittest.TestCase):
    
    def setUp(self):
        self.test_path = "/root/directory/subdirectory/zipdirectory"
        self.curr_dir = os.getcwd()
        self.curr_dir_base = os.path.basename(self.curr_dir)
        self.curr_dir_file_list = [fn for fn in os.listdir(self.curr_dir) if os.path.isfile(fn)]
        pass
            
    def test_directory_base(self):
        self.assertEqual(da.get_directory_base(self.test_path),'zipdirectory', "Path base name not equal")
        
    def test_zf_name(self):
        self.assertEqual(da.get_zf_name('zipdirectory'),'zipdirectory.zip', "Zip name not equal")
        
    def test_zf_path(self):
        self.assertEqual(da.get_zf_path(self.test_path,'zipdirectory.zip'), \
                         os.path.join(self.test_path,'zipdirectory.zip'), \
                         "Generated path not equal")
    def test_file_list(self):
        self.assertEqual(da.get_file_list(self.curr_dir),self.curr_dir_file_list, "File lists not equal")

    def test_directory_archive(self):
        """ Test to see if the list of files in the zip match the list of files
            in the directory, except for the zip file itself.
        """
        # Get the path of the zip file created
        zip_filename = da.directory_archive(self.curr_dir)
        # Open the zip file
        zf = zipfile.ZipFile(zip_filename)
        # Get list of the files in zip
        zf_files = zf.namelist()
        zf.close()
        # Adjust file list to remove head
        file_list = [os.path.basename(fn) for fn in zf_files]
        self.assertEqual(set(file_list), set(self.curr_dir_file_list), "Zip contents do not match directory")
        
    def tearDown(self):
        pass
    
if __name__ == "__main__":
    unittest.main()
    