'''
This code imports a module and will print a list of functions in the module
in the format of the function name and argument, as it would appear in a
def statement.
'''

import smtplib as m

import inspect

lst_of_functions = inspect.getmembers(m, inspect.isfunction)

for function in lst_of_functions:
    name, obj = function
    lst_of_args = inspect.formatargspec(*inspect.getfullargspec(obj))
       
    print("def {0}{1}:".format(name,lst_of_args))