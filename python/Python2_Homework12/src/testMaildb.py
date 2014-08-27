"""
Read in and parse email messages to verify readability.

NOTE: This test creates the message table, dropping any previous version
and should leave it empty. DANGER: this test will delete any existing message table
"""
from email import message_from_string
import mysql.connector as msc
from database import login_info
import maildb
import unittest
from datetime import timedelta
from email.utils import parsedate_tz, mktime_tz, make_msgid
from settings import *


conn = msc.Connect(**login_info)
curs = conn.cursor()

TBLDEF = """\
CREATE TABLE message (
     msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
     msgMessageID VARCHAR(128),
     msgDate DATETIME,
     msgRecipientName VARCHAR(128),
     msgRecipientAddress VARCHAR(128),
     msgText LONGTEXT
)"""
#FILESPEC = "C:/PythonData/*.eml"

class testRealEmail_traffic(unittest.TestCase):
    def setUp(self):
        """
        Reads an arbitrary number of mail messages and
        stores them in a brand new messages table.
        
        DANGER: Any existing message table WILL be lost.
        """
        curs.execute("DROP TABLE IF EXISTS message")
        conn.commit()
        curs.execute(TBLDEF)
        conn.commit()

        self.msgids = {} # Keyed by message_id
        self.message_ids = {} # keyed by id
        self.msgdates = []
        self.rowcount = 0
        message_template = """ 
        Date: {0}
        From: website@example.com
        To: {1}<{2}>
        Message-Id: <{3}>
        
        This is a test message.
        """       
        format_string = "%a, %d %b %Y %H:%M:%S %z"
        msgDate = STARTTIME
        delta = timedelta(1) # create a time delta of one day
        msgid = make_msgid("com.example.oreilly.python")
        
        for day in range(DAYCOUNT):
            for msgRecipientName, msgRecipientAddress in RECIPIENTS:
                text = message_template.format(msgDate.strftime(format_string),msgRecipientName,msgRecipientAddress, msgid )
                print("text is :", text)
            
                msg = message_from_string(text)
                print("message is:", msg)
                id = self.msgids[msg['message-id']] = maildb.store(msg)
                self.message_ids[id] = msgid
                self.rowcount += 1 #Assuming no duplicated Message-IDs
            self.msgdates.append(msgDate)               
            msgDate = msgDate + delta #add the timedelta to date


            
            

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
 
    def test_message_ids(self):
        """
        Verify that items retrieved by id have the correct Message-ID.
        """  
        for message_id in self.msgids.keys():
            pk, msg = maildb.msg_by_id(self.msgids[message_id]) 
            self.assertEqual(msg['message-id'], message_id)

    def test_ids(self):
        """
        Verify that items retrieved by message_id have the correct Message-ID.
        """
        for id in self.message_ids.keys():
            pk, msg = maildb.msg_by_message_id(self.message_ids[id])
            self.assertEqual(msg['message-id'], self.message_ids[id])
            
    def test_dates(self):
        """
        Verify that retrieving records between the minimum and maximum dates returns an appropriate number of records.
        """
        mind = min(self.msgdates)
        mindate = datetime.date(mind.year, mind.month, mind.day)
        maxd = max(self.msgdates)
        maxdate = datetime.date(maxd.year, maxd.month, maxd.day)
        self.assertEqual(self.rowcount, len(maildb.msgs(mindate = mindate, maxdate = maxdate)))

if __name__  == "__main__":
    unittest.main()
