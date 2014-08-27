"""
Test module for classFactory
"""

import unittest
from classFactory import build_row
from database import login_info
import mysql.connector



class DBTest(unittest.TestCase):
  
    def setUp(self):        
        C = build_row("animal", "id name family weight")
        self.c = C([9999, "Pixie", "Unicorn", 1800])        

      
    def test_attributes(self):
        """ Verify access to attributes on an instance of build_row """
        self.assertEqual(self.c.id, 9999)
        self.assertEqual(self.c.name, "Pixie")
        self.assertEqual(self.c.family, "Unicorn")
        self.assertEqual(self.c.weight, 1800)
        
    def test_repr(self):
        """ Verify __repr__ produces expected string representation of build_row instance """
        self.assertEqual(repr(self.c), 
                         "animal_record(9999, 'Pixie', 'Unicorn', 1800)")
        
    def test_retrieve(self):
        """ Verify retrieve with condition returns the correct number of records """
        db = mysql.connector.Connect(**login_info)
        cursor = db.cursor()
        
        # count the number of records in the table
        cursor.execute("SELECT COUNT(*) FROM animal")  
        row_count = cursor.fetchone()[0]
        
        # obtain a list of the values for the family column
        cursor.execute("SELECT DISTINCT family FROM animal")
        result = []
        for family in cursor.fetchall():
            result.append(family)
        
        # call retrieve for each family value and calculate sum total of records    
        count = 0
        for family in result:
            condition = "family = '{0}'".format(family)
            datarows = self.c.retrieve(cursor, condition)
            ret_row_count = len(self.c)
            count += ret_row_count
        # assert that the table row count is the same as the sum count of each family type   
        self.assertTrue(row_count, count)
        
if __name__== "__main__":
    unittest.main()