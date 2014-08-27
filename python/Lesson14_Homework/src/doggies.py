""" Lesson 14 Classes and Objects """

class Dog:
    
    def __init__(self, name, breed):
        # initialize attributes
        self.name = name
        self.breed = breed
    
    def __str__(self):
        # format attributes for string
        return "%s:%s" % (self.name, self.breed)
    
if __name__ == "__main__":
    dogs = [] # declare empty list
    while True:
        dogname = input('Name:')
        if dogname == '': # exit loop on blank name
            break
        dogbreed = input('Breed:')
        
        dogs.append(Dog(dogname,dogbreed)) # append entry to list
        
        for i, dog in enumerate(dogs): # print the current dogs list
            print("%s. %s" % (i, dog))
        print(30*'*')  
        