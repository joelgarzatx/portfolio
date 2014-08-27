"""
RECIPIENTS   a list of (name, email-address) tuples
STARTTIME    datetime.datetime object for first message
DAYCOUNT    number of daily message generations
"""

from datetime import datetime
from datetime import tzinfo



RECIPIENTS = [("bert", "bert@ss.com"), ("cookie", "cookie@ss.com"), ("ernie", "ernie@ss.com")]
STARTTIME = datetime(2014, 5, 6, 12, 0, 0)
DAYCOUNT = 10
