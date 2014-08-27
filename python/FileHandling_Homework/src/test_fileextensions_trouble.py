import os
import tempfile
import shutil

def test_1():
    "Verify that the current directory is empty"
    print(dirname)
             
def test_2():
    "Verify creation of files is possible"
    print(dirname)

def test_3():
    "Verify that the counts are the same"
    print(dirname)

def tearDown():
    os.chdir(origdir)
    print(dirname)
    shutil.rmtree(dirname)          

if __name__ == "__main__":
    #unittest.main()

    origdir = os.getcwd()
    dirname = tempfile.mkdtemp("testdir")
    os.chdir(dirname)
    print(dirname)
    
    test_1()
    test_2()
    test_3()
    tearDown()
    