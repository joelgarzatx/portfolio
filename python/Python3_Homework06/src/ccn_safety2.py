import re

def ccn_hide(text):
    return re.subn(r"\d{4}-\d{4}-\d{4}-(\d{4})", r"XXXX-XXXX-XXXX-\1", text)