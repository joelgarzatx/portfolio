
uin = input("Input your text:")
wordlist = uin.strip().split()

caplist = []
lowlist = []

for word in wordlist:
    if word.islower():
        lowlist.append(word)
    else:
        caplist.append(word)

newlist = caplist + lowlist

for word in newlist:
    print(word)
    