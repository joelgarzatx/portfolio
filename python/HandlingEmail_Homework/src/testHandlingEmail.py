import unittest
from HandlingEmail import make_MIME_multipart_message

class HandlingEmailTest(unittest.TestCase):
    
    def setUp(self):
        self.email = 'joel.garza@frozencactus.com'
        self.string = "This is a short email message. In will be the body of the message."
        self.file_list = ['text_file01.txt', 'text_file02.txt', 'python-logo.png']
        self.test_msg = make_MIME_multipart_message(self.email, self.string, self.file_list)        
        
    def test_address(self):
        self.assertEqual(self.test_msg['To'], self.email)
        self.assertEqual(self.test_msg['From'], self.email)
        
    def test_messagetype(self):
        self.assertTrue(self.test_msg.is_multipart())        

    def test_print_message(self):
        print(self.test_msg.as_string())


if __name__== "__main__":
    unittest.main()