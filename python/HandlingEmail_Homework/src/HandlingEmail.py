"""
Program accepts three arguments: address, string message, and file list
to compose a MIME Multipart message. Files may be type text or image, as recognized 
by the Python mimetypes module.
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import mimetypes
import datetime
import os

def make_MIME_multipart_message(address, message, file_list=None):
    msg = MIMEMultipart()
    msg['To'] = address
    msg['From'] = address
    msg['Date'] = datetime.datetime.now().strftime("%d %b %Y %H:%M:%S -0600") 
    msg.attach(MIMEText(message, 'plain'))
            
    if file_list:
        for fn in file_list:
            filepath = os.path.join('.',fn)

            if not os.path.isfile(filepath):
                continue

            type_guess, encoding = mimetypes.guess_type(filepath)

            main_type,sub_type = type_guess.split('/', 1)
            if main_type == 'text':
                fp = open(filepath)
                txt = MIMEText(fp.read(), sub_type)
                txt.add_header('Content-Disposition', 'attachment', filename=fn)
                msg.attach(txt)
            elif main_type == 'image':
                fp = open(filepath,'rb')
                img = MIMEImage(fp.read(), sub_type)
                img.add_header('Content-Disposition', 'attachment', filename=fn)
                msg.attach(img)
            fp.close()
    return msg
