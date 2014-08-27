small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')
def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """
    new_lst = []
    lst_of_words = title.lower().split()
    for word in lst_of_words:
        if word not in small_words:
            new_lst.append(word.capitalize())
        else:
            new_lst.append(word)
    new_lst[0] = new_lst[0].capitalize()           
    return " ".join(new_lst)

def _test():
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()