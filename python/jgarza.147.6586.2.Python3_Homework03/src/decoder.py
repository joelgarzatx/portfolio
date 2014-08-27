"""
Decoder provided function alphabator(list) accepts an integer list, 
which returns the list of integers, substituting letters of the alphabet
for integer values from 1 through 26
"""

def alphabator(number_list):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return (alphabet[x-1] if x in range(1,27) else x for x in number_list)
