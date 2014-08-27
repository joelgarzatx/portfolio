"""
classFactory: function to return tailored classes

"""

def build_row(table, cols):
    """ Build a class that creates instances of specific rows """
    class DataRow:
        """ Generic data row class, specialized by surrounding function """
        def __init__(self, data):
            """ Uses data and column names to inject attributes """
            assert len(data) == len(self.cols)
            for colname, dat in zip(self.cols, data):
                setattr(self, colname, dat)
            self._len = 1    # used to store the number in the collection following a call to retrieve
        
        def __repr__(self):
            return "{0}_record({1})".format(self.table, ", ".join(["{0!r}".format(getattr(self, c)) for c in self.cols]))
        
        def retrieve(self, curs, condition=None):
            """ Uses cursor and condition to retrieve records from database 
                represented by the DataRow class instance
            """
            query_string = "SELECT " + ", ".join(self.cols) + " FROM " + self.table
            if condition:
                query_string += " WHERE " + condition            
            curs.execute(query_string)  
            
            # set the length as the number of records returns, instead of exhausting the generator to count
            self._len = curs.rowcount   
            # generator to yield one returned record at a time         
            for row in curs.fetchall():
                datarow = DataRow(row)
                yield datarow
                
        def __len__(self):
            # implement the len() function to peek at the number of rows in the retrieve query
            return self._len
        
        
    DataRow.table = table
    DataRow.cols = cols.split()
    return DataRow