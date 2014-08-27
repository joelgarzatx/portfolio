"""
Decoder provided function alphabator(list) accepts an integer list, 
which returns the list of integers, substituting letters of the alphabet
for integer values from 1 through 26
"""

def alphabator(object_list):
    """ Accepts a list of objects and returns the objects from
        the list, replacing integer values from 1 to 26 with
        the corresponding letter of the English alphabet
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for object in object_list:
        if object in range(1,27): # object is integer from 1 - 26
            ret_val = alphabet[object-1] # grab corresponding letter from alphabet list
        else: # other integer value or object
            ret_val = object
        yield ret_val

