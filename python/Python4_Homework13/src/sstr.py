
class sstr(str):
        
    def __init__(self, string_val):
        super().__init__() # call __init__ from inherited class str
        self.string_val = string_val # store the value
        
    def __lshift__(self, shift_val): # implement standard method "left shift" for string
        return self.__shift_string(shift_val, "left")
    
    def __rshift__(self, shift_val): # implement standard method "right shift" for string
        return self.__shift_string(shift_val, "right")
    
    def __shift_string(self, shift_val, shift_dir="left"):
        """ Since left shift and right shift will share a bit of code, will implement in 
            separate function
        """

        try: # test that shift value is an integer
            shift_val = int(shift_val)
        except (TypeError):
            print("Error: Shift value must be a positive integer.")            
                  
        string_len = len(self.string_val)
        shift_val = shift_val % string_len # MODULO the shift value so shift_val is < string length
        
        if shift_val == 0: # return string unchanged if shift 0
            string_result = self.string_val
        else:
            if shift_dir == "right": # A right shift is the same as the complement from the string length
                shift_val = string_len - shift_val
            string_result = self.string_val[shift_val:] + self.string_val[:shift_val] 
        return sstr(string_result) # need to make sure return type is sstr to support shifting

if __name__ == "__main__":
    s = sstr("abcde")
    print("s is ", s)
    print("s << 0 is", s << 0)
    print("s >> 0 is", s >> 0)
    print("s << 2 is", s << 2)
    print("s >> 2 is", s >> 2)
    print("s >> 5 is", s >> 5)
    print("(s >> 5) << 5 is", (s >> 5) << 5)
    print("s >> -1 is", s >> -1)  # normally, in bit shifting, this is undefined behavior
    
          