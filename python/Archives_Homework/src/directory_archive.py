"""
A function that takes a directory path and creates an archive of the directory only.
If the directory contains subdirectories, the subdirectory names and any files in the 
subdirectories should not be included.
"""
import os
import zipfile


def directory_archive(path_to_files):
    """ Creates a zip file using the base from the path as the name of the
        zip file, and includes only the files from the directory using the
        base directory as the referential path       
    """

    files_to_archive = [f for f in os.listdir(path_to_files) if os.path.isfile(os.path.join(path_to_files,f))]  
    base = os.path.basename(path_to_files)    
    zip_filename = path_to_files + ".zip" # zip file is created in same directory as the subdirectory containing the files.            
    zf = zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED)    
    # loop through list of files, writing to the zip container
    for fn in files_to_archive:
        zf.write(os.path.join(path_to_files,fn), arcname = os.path.join(base,fn))
    zf.close()   
    return zip_filename

if __name__ == "__main__":
    zipped = directory_archive(os.path.dirname(os.path.abspath(__file__)))
    print(zipped)
    
