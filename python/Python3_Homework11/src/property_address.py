import re
import logging
LOG_FILENAME = "property_address.log"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
DEFAULT_LOG_LEVEL = "warning" # Default log level
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
        logging.info('Creating a new address')
        
    @property
    def name(self):
        return self._name
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        regex = re.compile('^[A-Z]{2}$')
        # State must be two capital letters
        result = regex.match(value)
        if not result:
            logging.error('STATE exception')
            raise StateError("Invalid State Code format! Must be two capital letters.")
        else:
            self._state = result.group()
            logging.info('Updating State value')
            
    @property
    def zip_code(self):
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, value):
        regex = re.compile('^\d{5}$')
        # Zip Code must be five digits
        result = regex.match(value)
        if not result:
            logging.error('ZIPCODE exception')
            raise ZipCodeError("Invalid Zip Code format! Must be five digits.")
        else:
            self._zip_code = result.group()
            logging.info('Updating Zip Code value')
    
        
        