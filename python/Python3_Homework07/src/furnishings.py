
class Furnishing(object):
    
    def __init__(self, room):
        self.room = room
        
class Sofa(Furnishing):
    def __init__(self, room):
        super().__init__(room)
        self.name = "Sofa"

class Bookshelf(Furnishing):
    def __init__(self, room):
        super().__init__(room)
        self.name = "Bookshelf"

class Bed(Furnishing):
    def __init__(self, room):
        super().__init__(room)
        self.name = "Bed"

class Table(Furnishing):
    def __init__(self, room):
        super().__init__(room)
        self.name = "Table"

def map_the_home(home):
    d = {}
    for item in home:
        try:
            d[item.room].append(item)
        except KeyError:
            d[item.room] = []
            d[item.room].append(item)
    return d

def counter(home):
    d = {'Bed':0,'Bookshelf':0,'Sofa':0,'Table':0}
    d_name = {'Bed':'Beds','Bookshelf':'Bookshelves','Sofa':'Sofas','Table':'Tables'}
    for item in home:
        d[item.name] += 1

    for furn, furn_count in sorted(d.items()):
        print("{0}: {1}".format(d_name[furn], furn_count))
    return d

if __name__ == "__main__":
    home = []
    home.append(Bed('Bedroom'))
    home.append(Sofa('Livingroom'))
    home.append(Table('Livingroom'))
    home.append(Table('Kitchen'))
    print(home)
    print(map_the_home(home))
    counter(home)