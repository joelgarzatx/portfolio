""" 
Program for optimization. Python 4, Lesson 5. 

Calculates the groffle speed of a knurl widget 
of average density given by user input. 
""" 

from math import log 
from timeit import Timer 

def groffle_slow(mass, density): 
    total = 0.0 
    for i in range(10000): 
        masslog = log(mass * density) 
        total += masslog/(i+1)

    return total

def groffle_fast(mass, density): 
    total = 0.0 
    temp_val = mass * density
    masslog = log(temp_val)
    for i in range(1,10001):        
        total += (masslog/i)
    
    return total


mass = 2.5 
density = 12.0 

print("Calculating groffle...")

gr_slow = groffle_slow(mass, density)
gr_fast = groffle_fast(mass, density)

print("Slow approach result is :", gr_slow)
print("Fast approach result is :", gr_fast)

try:
    assert(gr_slow == gr_fast)
except:
    print("The results are NOT the same!")
else:
    print("The results are the same.")
    
print("-" * 40)
print("Calculating time...")

timer1 = Timer("total = groffle_slow(mass, density)", 
 "from __main__ import groffle_slow, mass, density") 
print("time for slow approach:", timer1.timeit(number=1000)) 

timer2 = Timer("total = groffle_fast(mass, density)", 
 "from __main__ import groffle_fast, mass, density") 
print("time for fast approach:", timer2.timeit(number=1000)) 

import cProfile as profile
print("Profile for groffle_slow")
print("=" * 40)
profile.run("groffle_slow(mass, density)")
print("-" * 40)
print("Profile for groffle_fast")
print("=" * 40)
profile.run("groffle_fast(mass, density)")
