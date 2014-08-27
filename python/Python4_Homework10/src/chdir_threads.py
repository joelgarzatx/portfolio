'''
chdir_threads.py: Use threading to determine whether when the current directory is 
changed by one thread, if the current directory changes for other threads.

Specifically, will it change for a thread that existed before the change, and will 
it change for a thread create after the call.
'''

import threading
import time
import os

def run(i, name):
    """Sleep for a given number of seconds, report and terminate."""
    print(name,"now starting")
    cwd = os.getcwd()
    print(name,"current directory is", cwd)
    if i == 1:
        os.chdir(os.path.join(cwd,'a'))
        print(name,"changing the directory to", os.getcwd())
    time.sleep(4)
    print(name, " has finished")
    print(name,"current directory is", os.getcwd())

for i in range(3):
    t = threading.Thread(target=run, args=(i, "T"+str(i)))
    t.start()
    time.sleep(2)
print("Main done")
