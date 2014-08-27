import configparser
from optparse import OptionParser

import re
import logging

config = configparser.RawConfigParser()
config.read('v:/workspace/Python3_Homework12/src/propertyaddress.cfg')
ZIP_REGEX = config.get('validators', 'zip_code')
STATE_REGEX = config.get('validators', 'state')
LOG_FILENAME = config.get('log', 'output')
LOG_FORMAT = config.get('log', 'format')

DEFAULT_LOG_LEVEL = "info" # Default log level
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
         }

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    "Start logging with given filename and level."
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)

class StateError(Exception):
    pass

class ZipCodeError(Exception):
    pass

class Address(object):
    
    def __init__(self, name, street_address, city, state, zip_code):
        self._name = name
        self.street_address = street_address
        self.city = city
        self._state = state
        self._zip_code = zip_code
        # send state and zip values through custom setters
        self.state = self._state
        self.zip_code = self._zip_code
        logging.info('Creating a new address')
    
    def __str__(self):
        addr_string = "{0}\n{1}\n{2}, {3}  {4}".format(self.name, self.street_address, self.city, self.state, self.zip_code)
        return addr_string
    
    def __repr__(self):
        d = {'name':self.name, 'street_address':self.street_address, 'city':self.city, 'state':self.state, 'zip_code':self.zip_code}
        return d
    
    @property
    def name(self):
        return self._name
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        regex = re.compile(STATE_REGEX)
        # State must match pattern
        result = regex.match(value)
        if not result:
            logging.error('STATE exception')
            raise StateError("Invalid State Code format!")
        else:
            self._state = result.group()
            logging.info('Updating State value')
            
    @property
    def zip_code(self):
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, value):
        regex = re.compile(ZIP_REGEX)
        # Zip Code must match pattern
        result = regex.match(value)
        if not result:
            logging.error('ZIPCODE exception')
            raise ZipCodeError("Invalid Zip Code format!")
        else:
            self._zip_code = result.group()
            logging.info('Updating Zip Code value')
    
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-l', '--level', dest = "level", 
                      action = "store",
                      help = "sets the log level to DEBUG, INFO, WARNING, ERROR," + \
                      "and CRITICAL. Defaults to INFO." )
    parser.add_option('-n', '--name', dest = "name", action = "store",
                      help = "sets the name value of the Address object" )  
    parser.add_option('-a','--address', dest = "address", action = "store",
                      help = "sets the street_address value of the Address object") 
    parser.add_option('-c','--city', dest = "city", action = "store",
                      help = "sets the city value of the Address object")
    parser.add_option('-s','--state', dest = "state", action = "store",
                      help = "sets the state value of the Address object")
    parser.add_option('-z','--zip_code', dest = "zip_code", action = "store",
                      help = "sets the zip_code value of the Address object")         
    (options, args) = parser.parse_args()
    
    #validations
    if not (options.name and options.address and options.city and options.state and options.zip_code):
        parser.error("options -n, -a, -c, -s, -z are required")
    if options.level:
        if options.level in LEVELS.keys(): # verify log level supplied is valid option
            start_logging(level=options.level)
        else:
            parser.error("option -a requires value of:",",".join(LEVELS.keys()))
    else:
        start_logging() # uses default defined at top of code
            
    
    try:
        entry = Address(options.name, options.address, options.city, options.state, options.zip_code)
        print(entry)
        print(Address.__repr__(entry))
        
    except ZipCodeError:
        parser.error("option -z requires a valid 9-digit US zip code")
    except StateError:
        parser.error("option -s requires a valid 3-character US state code")
        