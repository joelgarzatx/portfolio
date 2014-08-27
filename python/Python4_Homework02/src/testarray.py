"""
Test list-of-list array implementations using tuple subscripting,
modified for three dimensions.
"""
import unittest
import arr

class TestArray(unittest.TestCase):
    """creates an array of each size and tests that values are zero"""
    def test_zeroes(self):
        for N in range(4):
            a = arr.array(N, N, N)
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i, j, k], 0)

    def test_identity(self):
        """creates an array of each size and verifies each as an identity matrix,
           where the value in location i, j, k, where i=j=k, is one, and zero elsewhere"""
        for N in range(4):
            a = arr.array(N, N, N)
            for i in range(N):
                a[i, i, i] = 1
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i, j, k], i==j==k)
                        
    def _index(self, a, r, c, s):
        """ accepts an array object, row, column, and slice as arguments and 
            returns the dictionary value at key [r, c, s], or KeyError if does not exist
        """
        return a[r,c,s]
    
    def test_key_validity(self):
        """ test confirms KeyError is raised for index range < 0 or 
            greater than max index of dimension """
        a = arr.array(10, 10, 10)
        self.assertRaises(KeyError, self._index, a, -1, 1, 1)
        self.assertRaises(KeyError, self._index, a, 1, -1, 1)
        self.assertRaises(KeyError, self._index, a, 1, 1, -1)
        self.assertRaises(KeyError, self._index, a, 10, 1, 1)
        self.assertRaises(KeyError, self._index, a, 1, 10, 1)
        self.assertRaises(KeyError, self._index, a, 1, 1, 10) 
               

if __name__ == "__main__":
    unittest.main()
