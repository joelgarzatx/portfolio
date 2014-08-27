'''
Prepare a subclass of the standard dict class. __init__ accepts one argument to
be used as the default value when a KeyError is raised.
'''


class Dict(dict):
    # initialize using provided value as default value for non-existent key
    def __init__(self,def_value):
        dict.__init__(self) # call standard dict's __init__ with no arguments
        self._def_value = def_value # assign the default value for this Dict
    def __getitem__(self, key):
        try: # catch KeyError for non-existent key and return the object's default value
            return dict.__getitem__(self, key)
        except KeyError:
            return self._def_value
        
if __name__ == "__main__":
    d = Dict("no luck, chuck")
    d['frank'] = "I did it my way"
    d['johnny'] = "It burns, burns, burns, that ring of fire"
    print(d)
    print(d['frank'])
    print(d['johnny'])
    print(d['spence'])
    