'''
adder.py: adder function that adds together two integer type object
Integer values as string or float are not accepted.
'''
import numbers

def adder(a, b):
    if isinstance(a, numbers.Integral) and isinstance(b, numbers.Integral):
        return a + b
    else:
        raise TypeError