"""
Program creates a ten megabyte data file in two different ways
and times each method.
"""

import sys
import time
import tempfile
import mmap

BYTE = 1
KB_128 = 131072 # I know, these are kibi and mebi
KB_256 = 262144
KB_512 = 524288
ONE_MB = 1048576 # Bytes
TWO_MB = 2097152
FIVE_MB = 5242880
TEN_MB = 10485760



file_size = TEN_MB
chunk_size = TWO_MB

for chunk_size in [BYTE, 8, 16, 64, 128, 256, 1024, 8192, KB_128, KB_256, KB_512, ONE_MB, TWO_MB, FIVE_MB]:

    passes = file_size // chunk_size
    chunk_data = b'\0' * chunk_size
    
    print("=" * 20)
    print("Pass for chunk size = ", chunk_size)
    print("-" * 20)

    # create a memory-mapped file and write the data by setting one chunk
    # at a time using successively higher indexes
    tempfil_b = tempfile.TemporaryFile('w+b')
    mapf = mmap.mmap(tempfil_b.fileno(),TEN_MB,access=mmap.ACCESS_WRITE)
    
    start_time = time.time()
    for chunk in range(passes):
        offset = chunk * chunk_size
        mapf[offset:offset + chunk_size] = chunk_data
    mapf.flush() # make sure the info is written to disk
    stop_time = time.time()
    time_to_run = stop_time - start_time
    print("Time to run using mmap indexing: ", time_to_run)
    
    # create an empty binary file and repeatedly use the write() method
    # to write a chunk of data, and get the time to complete
    tmpfil_a = tempfile.TemporaryFile('w+b') # using a temp file
    start_time = time.time()
    for chunk in range(passes):
        tmpfil_a.write(chunk_data)   
    sys.stdout.flush()    # make sure the info is written to disk
    stop_time = time.time()
    time_to_run = stop_time - start_time
    print("Time to run direct to file: ", time_to_run)
    
    

