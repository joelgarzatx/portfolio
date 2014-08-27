import re

def find_regex(target_string, pattern_string):
    """
    find_regex(target_string, pattern_string) returns the start 
    and end position of a pattern_string found in a target_string,
    or it returns None
    """
    
    m = re.search(pattern_string, target_string)
    if m:
        return (m.span())
    else:
        return None


if __name__ == "__main__":
    target_string = """
In the 1950s, mathematician Stephen Cole Kleene described automata theory and formal language theory in a set of models using a notation called "regular sets" as a method to do pattern matching. Activeusage of this system, called Regular Expressions, started in the 1960s and continued under such pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry Spencer.        
        """
    pattern_string = "Regular Expressions"
    print(find_regex(target_string,pattern_string))
    help(find_regex)
                