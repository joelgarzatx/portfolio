"""
Read in and parse email messages to verify readability.

NOTE: This test creates the message table, dropping any previous version
and should leave it empty. DANGER: this test will delete any existing message table
"""

import mysql.connector as msc
from database import login_info

import datetime
import jotd_mail
import unittest

from jotd_settings import STARTTIME, DAYCOUNT, RECIPIENTS

conn = msc.Connect(**login_info)
curs = conn.cursor()

TBLDEF = """\
CREATE TABLE message (
     msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
     msgMessageID VARCHAR(128),
     msgDate DATETIME,
     msgSenderName VARCHAR(128),
     msgSenderAddress VARCHAR(128),
     msgText LONGTEXT
)"""

class test_JotD(unittest.TestCase):
    def setUp(self):
        """
        Generates a set of joke emails for the number of days specified, addressed
        to the list of recipients.
        stores them in a brand new messages table.
        
        DANGER: Any existing message table WILL be lost.
        """

        self.recipient_count = len(RECIPIENTS)
        self.daycount = DAYCOUNT
        curs.execute("DROP TABLE IF EXISTS message")
        conn.commit()
        curs.execute(TBLDEF)
        conn.commit()        
        jotd_mail.generate_and_store_messages(STARTTIME, DAYCOUNT, RECIPIENTS)

    def test_not_empty(self):
        """
        Verify that the setUp method actually created some messages.
        If it finds no files there will be no messages in the table,
        the loop bodies in the other tests will never run, and potential
        errors will never be discovered.
        """
        curs.execute("SELECT COUNT(*) FROM message")
        messagect = curs.fetchone()[0]
        self.assertGreater(messagect, 0, "Database message table is empty")
         
    def test_record_count(self):
        """
        Verify that retrieving records returns an appropriate number of records.
        """
        curs.execute("SELECT COUNT(*) FROM message")
        messagect = curs.fetchone()[0]                
        self.assertEqual(messagect, len(RECIPIENTS) * DAYCOUNT)
        
    def test_message(self):
        from_address = 'from@email.com'
        to_address = 'to@email.com'
        msg_date = datetime.datetime(2014,8,10)
        
        test_msg = jotd_mail.make_MIME_multipart_message(to_address,from_address,msg_date,'This is a test.')
        self.assertEqual(test_msg['To'], to_address)
        self.assertEqual(test_msg['From'], from_address)

if __name__  == "__main__":
    unittest.main()
