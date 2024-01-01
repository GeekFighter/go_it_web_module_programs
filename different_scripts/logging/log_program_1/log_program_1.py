import logging

logging.basicConfig(level=logging.CRITICAL) # Налаштування рівня журналювання на CRITICAL

# print a log message to the console.
logging.debug('This is a debug level!') # виводить повідомлення рівня DEBUG.
logging.info('This is a info level!') # виводить повідомлення рівня INFO.
logging.warning('This is a warning level!') # виводить повідомлення рівня WARNING.
logging.error('This is an error level!') # виводить повідомлення рівня ERROR.
logging.critical('This is a critical level!') # виводить повідомлення рівня CRITICAL.