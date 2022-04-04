#! python3

# The shebang line tells your computer that you want to run the script using Python 3.
# On Windows, you can bring up the Run dialog by pressing Win+R.
# A batch file can save you a lot typing by running multiple commands.
# The batch files you'll make will look like this:
#     @py C:\Users\Al\MyPythonScripts\hello.py %*
#     @pause
# You'll need to add the MyPythonScripts folder to the PATH environment variable first.
# Command-line arguments can be read in the sys.argv list. (Import the sys module first.)

# The first line of all your Python programs should be a shebang line, which
# tells your computer that you want Python to execute this program. The she-
# bang line begins with #!, but the rest depends on your operating system.
# On Windows, the shebang line is #! python3.
# On OS X, the shebang line is #! /usr/bin/env python3.
# On Linux, the shebang line is #! /usr/bin/python3.

# You will be able to run Python scripts from IDLE without the shebang
# line, but the line is needed to run them from the command line.


print("Hello, World!")

# on cmd type
# cmd current location: C:\Users\username\
# py.exe "filename_with_directory.py"

# on run window type:
# py "filename_with_directory.py"
# program executes and closes fast

# on cmd type:
# pause.exe
# shows press any key to continue...

# creating batch/bat file. type inside:
# @py filelocation.py %*
# @pause

# @: tells computer not to display the line
# %*: tells computer to forward any command line arguments

# @pause: you can avoid it if there is no output in the program
# pyw: to make a windowless program. it makes the command line not appear when you run it. output will not be shown.

# we can avoid typing the location of the bat file in run window by adding that location in environment variable.
# On windows: goto control panel>system>advanced system settings>advanced tab>environment variables
# under system variables find the Path and click on edit and add new location of the folder in which the file is in.


# passing command line arguments: %* is required for this. Import sys module
import sys

print(
    sys.argv
)  # prints the list of command line arguments as strings, first item in the list is the location of python file
