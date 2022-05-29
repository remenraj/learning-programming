# The logging module lets you display logging messages.
# Log messages create a "breadcrumb trail" of what your program is doing.
# After calling logging.basicConfig() to set up logging, call logging.debug(‘This is the message') to create a log message.
# When done, you can disable the log messages with logging.disable(logging.CRITICAL)
# Don't use print() for log messages: It's hard to remove the mall when you're done debugging.
# The five log levels are: DEBUG, INFO, WARNING, ERROR, and CRITICAL.
# You can also log to a file instead of the screen with the filename keyword argument in the logging.basicConfig() function.

import logging

# # level: DEBUG, INFO, WARNING, ERROR, CRITICAL
# # basic config function
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# instead of writing to the screen, logging messages are written into the file
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# disable logging
# there are five levels: (lowest)DEBUG, INFO, WARNING, ERROR, CRITICAL(highest)

# line below disables all logging messages that are less than or equal to the CRITICAL level
logging.disable(level=logging.CRITICAL)   # comment this line to enable logging