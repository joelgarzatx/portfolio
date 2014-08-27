""" 
Lesson 16 Project 2 - read a text file and print a table showing word count for 
each of the word lengths encountered.

Steps
* get filename from args
* read file
* split into words
* count letters in each word, accounting for punctuation (function)
* add to a data structure for cumulative count
* print table
* print chart

Adjusts vertical scale based on largest word count. Values less than first
minor tick are not visible. For example, if minor tick is 20, a value of 
15 will not register. An alternative approach would be to change the '+'
to a '0' for x-axis labels where count is zero.

I get the feeling this is in dire need of refactoring, but I must trudge on! ;-)
"""
import sys
import math

def letter_count(word):
    """ 
    Return the count for the number of non-punctuation characters in a word 
    using a pre-selected string of punctuation. Numbers will be treated as words.
    
    >>> letter_count('five')
    5
    
    >>> letter_count("What's")
    5
    
    >>> letter_count("&")
    0
    
    >>> letter_count("$5,000.00")
    6
    
    """
    count = 0
    # Could have used string.punctation instead of string of punctuation_marks
    # Counting letters in each word vs stripping punctuation from file and counting word length
    punctuation_marks = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)"""
    for c in word:
        if c not in punctuation_marks:
            count += 1
    return count


if __name__ == "__main__":
    # Get the filename passed as first argument, index 0 is the name of py file
    try:
        filename = sys.argv[1]
        f = open(filename,"r")
    except Exception as msg:
        print ("Problem: {0}".format(msg))
        sys.exit()
    else:
        lines = f.readlines()
        f.close()
    # Initialize dictionary for storing counts for each word of each length   
    d = {}    
    for line in lines:
        words = line.split()
        for word in words:
            word_length = letter_count(word)
            if word_length not in d:
                # we don't want to keep track of 0 length "words"
                # of single punctuation, like &
                if word_length != 0:
                    d[word_length] = 1
            else:
                d[word_length] += 1
       
    # Print summary table
    print("Length Count")
    lengths = sorted(d.keys())
    for length in lengths:
        print(length,d[length])
    print()
    
    # Print histogram
    # Maximum word length
    xmax = lengths[-1]

    # Maximum word count
    ymax = max(d.values())
 
    
    # Hack to round to the next highest round number
    # Grab most significant digit, add 1, and multiply by a power of 10
    powerof10 = len(str(ymax)) - 1
    most_sig_digit = int(str(ymax)[0])
    yscale_max = (most_sig_digit + 1) * 10**powerof10
    
    # Calculate the minor tick scale
    yscale_minor = math.ceil(2 * 10**(powerof10 - 1))

    # Define the format string for the chart rows
    fmt = "{0:>" + str((powerof10 + 2)) + "} {1}{2}"
    
    for i in range(yscale_max, 0, -yscale_minor):
        chartrow = ""
        # Determine whether to include a layer in the column
        # based on the magnitude of the value
        for j in range(1, xmax + 1):
            if ((j in lengths) and (d[j] > i)):
                chartrow += "***"
            else:
                chartrow += "   "
                
        # Add major tick label
        if i % (10**powerof10) == 0:
            print(fmt.format(i,"-|", chartrow))
        else:
            print(fmt.format(" "," |", chartrow))
            
    # Finish off the x-axis of the chart
    chartrow = "-+-" * (xmax)
    print(fmt.format(0,"-+", chartrow))
    
    # Print x-axis labels
    chartrow = ""  
    for k in range(1,xmax + 1):
        chartrow += "{0:^3}".format(k)
    print(fmt.format(" "," |",chartrow))
         
# All done

        
            
    
    
    
    
    
            
        
    