# This version took me 30 minutes
import sys

def print_capitalize(text):
    """ 
    Accepts a string parameter and applies the capitalize() method. 
    """
    print(text.capitalize())
    
def print_title(text):
    """
    Accepts a string parameter and applies the title() method.
    """
    print(text.title())
    
def print_upper(text):
    """
    Accepts a string parameter and applies the upper() method.
    """
    print(text.upper())
    
def print_lower(text):
    """
    Accepts a string parameter and applies the lower() method.
    """
    print(text.lower())
    
def quit(text):
    """
    Ends the program
    """
    print("Goodbye for now!")
    sys.exit()
    
if __name__ == "__main__":
    switch = {
              'capitalize': print_capitalize,
              'title': print_title,
              'upper': print_upper, 
              'lower': print_lower,
              'exit': quit
              }
    options = switch.keys()
    prompt = 'Enter a function name ({0}): '.format(', '.join(options))
    while True:
        inp = input(prompt)
        option = switch.get(inp, None)
        # preserved the check for valid options from the lesson
        if option:
            # Deviation from assignment, wanted to catch 'exit' and skip second prompt
            if option != switch.get('exit', None):
                inp = input('Enter a sting:')
            option(inp)
        else:
            print('Please choose an available function!')