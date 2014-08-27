"""
API for coconut weights
"""

# [item for item in a if item[0] == 1]

class Coconut:    
    def __init__(self, coconut_type):
        """
        Create a coconut object. Valid type are "South Asian", "Middle Eastern", and "American"
        """
        self.coconut_types = (("South Asian", 3), ("Middle Eastern", 2.5), ("American", 3.5))
        d = dict(self.coconut_types)
        if coconut_type in d:
            self.coconut_type = coconut_type
            self.coconut_weight = d[coconut_type]
        else:
            raise KeyError("'%s' is not a valid type of coconut" % coconut_type)
            
class Inventory: 
    def __init__(self):
        self.inventory = []
    
    def add_coconut(self, coconut):
        """
        Add a coconut to the inventory
            coconut is an instance of coconut object
        """
        if isinstance(coconut,Coconut):
            self.inventory.append(coconut)
        else:
            raise AttributeError("Not a valid coconut object!")
            
    def total_weight(self):
        """
        Calculate the total weight of the coconut inventory
            algorith: sum of (# coconut_type * coconut_type_weights)
        """
        weight = 0
        for nut in self.inventory:
            weight += nut.coconut_weight
        return weight
    
    def inventory_list(self):
        """
        Print in an attractive format the list of coconuts in inventory.
        """
        text = ""
        for nut in self.inventory:
            text += "%s: %s\n" % (nut.coconut_type, nut.coconut_weight)
        return text
    
if __name__ == "__main__":
    c = Coconut("American")
    i = Inventory()
    help(c)
    help(i)
        
            
    