# You can raise your own exceptions: raise Exception(‘This is the error message.')
# You can also use assertions: assert condition, ‘Error message'
# Assertions are for detecting programmer errors that are not meant to be recovered from.
# User errors should raise exceptions.

import traceback


# # raise an exception
# raise Exception('This is the error message.')


# # writing the error message into a file
# try:
#     raise Exception("This is the error message.")

# except:
#     errorFile = open("error_log.txt", "a")
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print("The traceback info was written to error_log.txt")



# # # assert condition, ‘Error message’
# assert False, "This is the error message."

