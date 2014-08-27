import re

def ccn_hide(text):
    regex = re.compile(r"""
        \d{4}-   # the first four digits and dash
        \d{4}-   # the second four digits and dash
        \d{4}-   # the third four digits and dash
        \d{4}    # the final four digits
        """, re.VERBOSE)
    return regex.subn(r"CCN REMOVED FOR YOUR SAFETY", text)

if __name__ == "__main__":
    text = """Have you ever noticed, in television and movies, that phone numbers and credit cards 
    are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a 
    number that appears to be real, such as 1234-5678-1234-5678, triggers the attention of 
    privacy and security experts.
    """
    
    result = ccn_hide(text)
    print(result[0])