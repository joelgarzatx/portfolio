'''
tree.py
'''

class Tree:
    def __init__(self, key, value = None):
        "Create a new Tree object with empty L & R subtrees."
        self.key = key
        self.value = value
        self.left = self.right = None
    
    def insert(self, key, value = None):
        "Insert a new element into the tree in th ecorrect position."
        if key < self.key:
            if self.left:
                self.left.insert(key, value)
            else:
                self.left = Tree(key, value)
        elif key > self.key:
            if self.right:
                self.right.insert(key, value)
            else:
                self.right = Tree(key, value)
        else:
            raise ValueError("Attempt to insert duplicate value")
        
    def walk(self):
        "Generate the keys from the tree in sorted order."
        if self.left:
            for n in self.left.walk():
                yield n
        yield self.key
        if self.right:
            for n in self.right.walk():
                yield n

    def walk_with_data(self):
        "Generate the keys from the tree in sorted order."
        if self.left:
            for n in self.left.walk_with_data():
                yield n
        yield self.key, self.value
        if self.right:
            for n in self.right.walk_with_data():
                yield n
                                
    def find(self, key):
        "Look for a key in the tree and return the data, if any"
        value = None
        if key < self.key and self.left:
            value = self.left.find(key)
        elif key > self.key and self.right:
            value = self.right.find(key)
        elif key == self.key:
            value = self.value
        else:
            raise KeyError("Attempt to find key")
        return value        
                
if __name__ == "__main__":
    t = Tree("D")
    for c in "BJQKFAC":
        t.insert(c)
    t.insert("E", "secret")   
    print(list(t.walk()))
    print(list(t.walk_with_data()))
    
    for key in "AEZ":
        try:
            print(t.find(key))
        except KeyError:
            print("Unable to find key in tree")
