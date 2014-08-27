"""
control.py: Creates queues, starts output and worker processes, 
and pushes inputs into the input queue.
"""

from multiprocessing import Queue, JoinableQueue
from output import OutThread
from worker import WorkerThread
import random  
import time  
import sys

if __name__== "__main__":
    
    WORKERS = 10

    def random_1K_alpha_string():
    
        alpha_chars = "abcdefghijklmnopqrstuvwxyz"
        # use random.choice to select from the list of chars, then join list elements
        alpha_string = ''.join([random.choice(alpha_chars) for _ in range(1000)])
        return alpha_string
    
    begin = time.time() # Capture the starting time for time to run
    
    inq = JoinableQueue(maxsize=int(WORKERS*1.5))
    outq = Queue(maxsize=int(WORKERS*1.5))
    
    ot = OutThread(WORKERS, outq)
    ot.start()
    
    for i in range(WORKERS):
        w = WorkerThread(inq, outq)
        w.start()
    instring = random_1K_alpha_string()

    # feed the process pool with work units
    for work in enumerate(instring):
        inq.put(work)
    # terminate the process pool
    for i in range(WORKERS):
        inq.put(None)
    inq.join()
    
    finish = time.time() # Capture the stop time for time to run
    time_to_run = finish - begin # Subtract the calculate elapsed time
    sys.stdout.flush() # added to ensure process messages written to stdout before summary
    print("Run time in seconds: ", time_to_run)
    print("Control process terminating")