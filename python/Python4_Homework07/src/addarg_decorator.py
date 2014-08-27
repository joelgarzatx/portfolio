
def addarg(first_arg):
    "Returns a decorator that inserts a first argument."
    def func_dec(f):
        "Decorates a function to insert a first argument"
        def func_prepend(*args, **kwargs):
            "Inserts a first argument"
            return f(first_arg, *args, **kwargs)
        return func_prepend
    return func_dec

@addarg(1)        
def prargs(*args):
    return args

@addarg(10)
def prargsnkwargs(*args, **kwargs):
    return args, kwargs    

if __name__ == "__main__":

    
    print(prargs(2,3))
    print(prargs("child"))
    print(prargsnkwargs(2,3,name="bob", job="foreman"))
    