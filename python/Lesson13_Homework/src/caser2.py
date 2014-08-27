# This version took me 45 minutes, struggled with the correct
# formatting of the functions in the dictionary

import sys

def quit(text):
    """
    Ends the program
    """
    print("Goodbye for now!")
    sys.exit()
    
if __name__ == "__main__":
    switch = {
              'capitalize': str.capitalize,
              'title': str.title,
              'upper': str.upper, 
              'lower': str.lower,
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
            print('{0}'.format(option(inp)))
        else:
            print('Please choose an available function!')