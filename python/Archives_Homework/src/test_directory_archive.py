import unittest
import directory_archive as da
import os
import shutil
import zipfile

class TestZip(unittest.TestCase):
    """ Tests directory_archive.py : verifies file names in zip file 
        reflect the file contents of the folder being zipped.
    """
    
    def setUp(self):
        root = "v:\\workspace"
        sub = "zip_file_test"
        zip_folder = "zip_me_up"
        self.path_to_sub = os.path.join(root, sub) # directory where subfolder is and zip file will be created
        self.path_to_files = os.path.join(root,sub,zip_folder)
        self.zip_filename = os.path.join(root, sub, (zip_folder + ".zip"))
        
        # build folders for test suite
        os.mkdir(self.path_to_sub)
        os.mkdir(self.path_to_files)
        
        # create the sample files
        for fn in ["larry","moe","curly"]:
            f = open(os.path.join(self.path_to_files,fn), "w")
            f.write(fn)
            f.close()
        # retrieve the list of files that should be in the zip archive    
        self.curr_dir_file_list = ['/'.join([zip_folder,fn]) for fn in os.listdir(self.path_to_files) if os.path.isfile(os.path.join(self.path_to_files,fn))]



    def test_directory_archive(self):
        """ Test to see if the list of files in the zip match the list of files
            in the directory, except for the zip file itself.
        """
        # Get the path of the zip file created
        zip_filename = da.directory_archive(self.path_to_files)
        # Open the zip file
        zf = zipfile.ZipFile(zip_filename)
        # Get list of the files in zip
        zf_files = zf.namelist()
        zf.close()
        self.assertListEqual(zf_files, self.curr_dir_file_list, "Zip contents do not match directory")
        
    def tearDown(self):
        """ Removes the test files and folder path """
        os.remove(self.zip_filename)
        try:
            shutil.rmtree(self.path_to_sub, ignore_errors=True)
        except:
            pass


    
if __name__ == "__main__":
    unittest.main()
    