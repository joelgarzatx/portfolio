"""
A function that takes a directory path and creates an archive of the directory only.
If the directory contains subdirectories, the subdirectory names and any files in the 
subdirectories should not be included.
"""
import os
import zipfile

def get_directory_base(path):
    """ returns a string for the basename from the path """
    return os.path.basename(path)

def get_zf_name(directory_base):
    """ returns a string concatenating the basename with the '.zip' extension """
    return directory_base + '.zip'

def get_zf_path(path,zf_name):
    """ returns a string containing the full path of the zip file to create """
    return os.path.join(path,zf_name)

def get_file_list(path):
    """ returns a string from the list of files in the path, files only, no subdirectories """
    return [fn for fn in os.listdir(path) if os.path.isfile(fn)]


def directory_archive(path):
    """ Creates a zip file using the base from the path as the name of the
        zip file, and includes only the files from the directory using the
        base directory as the referential path
    """
    
    directory_base = get_directory_base(path)
    zf_name = get_zf_name(directory_base)
    zf_path = get_zf_path(path, zf_name)
    files_to_archive = get_file_list(path)
           
    zf = zipfile.ZipFile(zf_path, "w", zipfile.ZIP_DEFLATED)
    for fn_to_archive in files_to_archive:
        zf.write(os.path.join(path,fn_to_archive), arcname = os.path.join(directory_base,fn_to_archive))
    zf.close()
    return zf_path

if __name__ == "__main__":
    zipped = directory_archive(os.path.dirname(os.path.abspath(__file__)))
    print(zipped)
    
