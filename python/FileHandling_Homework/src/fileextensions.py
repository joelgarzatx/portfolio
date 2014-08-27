"""
Examines the contents of the current working directory and prints out a 
count of how many files have each extension.
"""
import os


def print_file_ext_count(path="."):  
    file_list = os.listdir(path)
    
    d = {}
    for file in file_list:
        extension = os.path.splitext(file)[1]
        if extension not in d.keys():
            d[extension] = 1
        else:
            d[extension] += 1
    for ext in sorted(d.keys()):
        print(ext, ":", d[ext])

    return list(d.items())

if __name__ == "__main__":
    print_file_ext_count()
    
