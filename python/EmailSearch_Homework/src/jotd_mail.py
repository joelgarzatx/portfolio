"""
   Joke-of-the-Day Python app -- takes a list of recipients, a start date, and a number of days to generate
       a set of email messages, inserted into the message table in the database
       
"""


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import make_msgid
import jotd_maildb
from datetime import timedelta
import time

def make_MIME_multipart_message(to_address, from_address, date, message):
    """ Accept addresses, date of message and message text.
        Returns MIME message.
    """
    msg = MIMEMultipart()
    msg['Date'] = date.strftime("%d %b %Y %H:%M:%S -0600")
    msg['From'] = from_address     
    msg['To'] = to_address
    msg['Message-Id'] = make_msgid('jotdmailblast')
    msg.attach(MIMEText(message, 'plain'))            
    return msg

def generate_and_store_messages(start_date, day_count, recipients_list, from_address='website@example.com'):
    """ Accept start date, number of days, recipients as list, optional from address.
        Stores messages in database, in message table.
    """
    for day_number in range(day_count):
        message_date = start_date + timedelta(days=day_number)
        message_text = get_joke()
        for user, to_address in recipients_list:
            my_msg = make_MIME_multipart_message( to_address, from_address, message_date, message_text )
            jotd_maildb.store(my_msg) 
            
def get_joke():
    """ Function to return joke message. Placeholder for later connection to joke database. """
    return "This is a test message."   

if __name__ == "__main__":
    from jotd_settings import STARTTIME, DAYCOUNT, RECIPIENTS
    start = time.time()
    generate_and_store_messages(STARTTIME, DAYCOUNT, RECIPIENTS)
    end=time.time()
    interval = end-start
    print("Time to complete: ", interval)
    print("Daycount: ", DAYCOUNT)
    
# Daycount: 1, 0.0759999752045
# Daycount: 10, 0.657999992371
# Daycount: 50, 3.16900014877
# Daycount: 100, 6.34500002861
# Daycount: 500, 27.6419999599 




