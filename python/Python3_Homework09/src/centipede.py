"""
Demonstrate magic methods for Python3_Lesson09
"""
class Centipede:
    def __init__(self):
        # Since modifying __setattr__ need to add directly to __dict__
        self.__dict__['stomach'] = []
        self.__dict__['legs'] = []
        
    def __setattr__(self,key,value):
        if key in ('stomach','legs'):
            # 'stomach' and 'legs are internal use only
            message = "{0!r} is for internal use only".format(key)
            raise AttributeError(message)
        else:
            # each time an attribute is set, append to internal list 'legs'
            self.__dict__[key] = value
            self.__dict__['legs'].append(key)
        
    def __call__(self, arg):
        # when called append argument to internal list 'stomach'
        self.__dict__['stomach'].append(arg)
        
    def __str__(self):
        # print() class returns comma-delimited string of list 'stomach'
        message = ",".join(self.stomach)
        return message
    
    def __repr__(self):
        # representation of centiped is command delimited string of list 'legs'
        message = ",".join(self.legs)
        return message
        
