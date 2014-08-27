"""
Sample program to list messages by date.
"""

from database import login_info
import mysql.connector
from email import message_from_string
from email.utils import formatdate, make_msgid
from settings import *
from datetime import *



message_template = """ 
Date: {0}
From: website@example.com
To: {1}<{2}>
Message-Id: <{3}>

This is a test message.
"""

conn = mysql.connector.Connect(**login_info)
curs = conn.cursor()

format_string = "%a, %d %b %Y %H:%M:%S"
msgDate = STARTTIME
delta = timedelta(days=1) # create a time delta of one day

msgid = 'message-id'

for day in range(DAYCOUNT):
    for msgRecipientName, msgRecipientAddress in RECIPIENTS:
        text = message_template.format(msgDate.strftime(format_string),msgRecipientName,msgRecipientAddress, make_msgid("com.example.oreilly.python"))
        msg = message_from_string(text)
        print(msg)
    msgDate = msgDate + delta #add the timedelta to date
    
    
#curs.execute("SELECT msgText FROM message ORDER BY msgDate")
#for text, in curs.fetchall():
#    msg = message_from_string(text)
#    print(msg['date'], msg['subject'])