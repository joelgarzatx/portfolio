s = set() # Create empty set
d = {} # Create empty dictionary

while True:
    uin = input("Enter text: ") 
    if uin == "": # Check for Enter keypress without any text and exit with message
        print("Finished")
        break

    uinlist = uin.strip().lower().split() # Create a list of the words in the string
    
    for word in uinlist:
        if word not in s: # Check to determine if this is a new word, since duplicates eliminated
            s.add(word) # Add new word to the set
            d[word] = len(s) # Add the new word to the dictionary and set the value to the number of words in the set
    for word in d.keys(): # Loop the dictionary to print the keys and values
        print(word,d[word])
        