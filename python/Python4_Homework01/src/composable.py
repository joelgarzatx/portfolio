"""
composable.py: defines a composable function class.
"""

import types

class Composable:
    def __init__(self, f):
        "Store reference to proxied function."
        self.func = f
        
    def __call__(self, *args, **kwargs):
        "Proxy the function, passing all arguments through."
        return self.func(*args, **kwargs)
    
    def __mul__(self, other):
        "Return the composition of proxied and another function."
        if type(other) is Composable:
            def anon(x):
                return self.func(other.func(x))
            return Composable(anon)
        elif type(other) is types.FunctionType:
            def anon(x):
                return self.func(other(x))
            return Composable(anon)
        raise TypeError("Illegal operands for multiplication")
    
    def __pow__(self,power):
        "Return function raised to a positive power"
        if power < 1:
            raise ValueError("Integer power should be positive, 1 or greater")
        elif not isinstance(power, int):
            raise TypeError("Positive power should be an integer, 1 or greater")
        elif power == 1:
            def anon(x):
                return self.func(x)
            return Composable(anon)
        else:
            def anon(x):
                return self.func(x) 
            temp_func = Composable(anon)
            for i in range(1,power):
                temp_func = temp_func * Composable(anon)                       
            return temp_func
        
    def __repr__(self):
        return "<Composable function {0} at 0x{1:x}>".format(self.func.__name__, id(self))