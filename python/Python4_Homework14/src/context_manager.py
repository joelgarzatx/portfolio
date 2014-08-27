"""
Python 4: Lesson 14, Project 1
"""
from contextlib import contextmanager

@contextmanager
def ctx_man(raising = True):
    """
    A context manager class, based on the example in Lesson 14, that suppresses
    any ValueError exceptions that occur in the controlled suite. Other exceptions
    will be raised in the surrounding context.
    """
    try:
        cm = object()
        print("Context manager returns:", id(cm))
        yield cm
        print("With concluded normally")
    except ValueError: # Suppress ValueError exception to allow context to finish normally
        print("Suppressing ValueError exception")
        pass
    except Exception as e: # If instance is raising, raise the except in the surrounding context
        print("Exception", e, "raised")
        if raising:
            print("Re-raising exception")
            raise

def err_raising_experience(exception):      
    with ctx_man(True) as cm:
        print("Raising exception", exception)
        raise exception  
    # Only get here if the error is not raised to the surrounding context
    return True
        