"""
output.py: The output process for the miniature framework
"""

identity = lambda x: x

import multiprocessing
import sys

class OutThread(multiprocessing.Process):
    def __init__(self, N, q, sorting=True, *args, **kw):
        """Initialize process and save queue reference."""
        multiprocessing.Process.__init__(self, *args, **kw)
        self.queue = q
        self.workers = N
        self.sorting = sorting
        self.output = []
    def run(self):
        """Extract items from the output queue and print until all done."""
        while self.workers:
            p = self.queue.get()
            if p is None:
                self.workers -= 1
                
            else:
                # This is a real output packet
                self.output.append(p)

        # place print string beneath loop to run upon the last thread terminating
        print("Final string length is: ", len(self.output))  
        sys.stdout.flush()  