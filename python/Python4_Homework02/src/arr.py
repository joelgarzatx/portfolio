

"""
Class-based dict allowing tuple subscripting & sparse data
modified for three dimensions

"""

class array:

    def __init__(self, M, N, O):
        "Create an M-element list of N-element row lists of O-element columns."
        self._data = {}
        self._rows = M
        self._cols = N
        self._slyce = O

    def __getitem__(self, key):
        "Returns the appropriate element for a three-element subscript tuple."
        row, col, slyce = self._validate_key(key)
        try:
            return self._data[row, col, slyce]
        except KeyError:
            return  0
    
    def __setitem__(self, key, value):
        "Sets the appropriate element for a three-element subscript tuple."
        row, col, slyce = self._validate_key(key)
        self._data[row, col, slyce] = value
    
    def _validate_key(self, key):
        """Validates a key against the array's shape, returning good tuples.
        Raises KeyError on problems."""
        row, col, slyce = key
        if (0 <= row < self._rows and
                0 <= col < self._cols and
                0 <= slyce < self._slyce):
            return key
        raise KeyError("Subscript out of range")
