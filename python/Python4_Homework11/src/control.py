"""
control.py: Creates queues, starts output and worker threads, 
and pushes inputs into the input queue.
"""

from queue import Queue
from output import OutThread
from worker import WorkerThread
import random  
import time  


WORKERS = 10

def random_1K_alpha_string():

    alpha_chars = "abcdefghijklmnopqrstuvwxyz"
    # use random.choice to select from the list of chars, then join list elements
    alpha_string = ''.join([random.choice(alpha_chars) for _ in range(1000)])
    return alpha_string

begin = time.time() # Capture the starting time for time to run

# create Queue objects for the input queue and output queue
inq = Queue(maxsize=int(WORKERS*1.5))
outq = Queue(maxsize=int(WORKERS*1.5))

# create and start the ouput thread
ot = OutThread(WORKERS, outq)
ot.start()

# create and start the worker threads
for i in range(WORKERS):
    w = WorkerThread(inq, outq)
    w.start()
    
# add work items
instring = random_1K_alpha_string()
for work in enumerate(instring):
    inq.put(work)
for i in range(WORKERS):
    inq.put(None)
inq.join() # wait for work threads to finish

finish = time.time() # Capture the stop time for time to run
time_to_run = finish - begin # Subtract the calculate elapsed time
print("Run time in seconds: ", time_to_run)
print("Control thread terminating")