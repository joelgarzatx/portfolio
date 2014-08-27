import unittest
import introgui

class TestGui(unittest.TestCase):
    
    def test_blank(self):
        self.assertEqual(introgui.float_sum("",3.0), "***ERROR***", "Error not raised")
    
    def test_alpha(self):
        self.assertEqual(introgui.float_sum("a",3.0), "***ERROR***", "Error not raised")
    
    def test_integer(self):
        self.assertAlmostEqual(introgui.float_sum(1.0,5),6.0, places=1, msg="Results not Equal")
        
    def test_real(self):
        self.assertAlmostEqual(introgui.float_sum(2.3456789, 5000.9876532), 5003.3333321, places=7, msg="Results not Equal")
    
if __name__ == "__main__":
    unittest.main()