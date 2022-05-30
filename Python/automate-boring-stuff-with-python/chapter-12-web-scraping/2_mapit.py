# Open google maps link with address taken from command line arguments/clipboard
# Run using bat file:
# create a bat file with the following content:
    # @py.exe  c:\dir\mapit.py %*

import webbrowser, sys, pyperclip


# check if command line arguments were passed
if len(sys.argv) > 1:
    # ["mapit.py", "870", "Valencia", "St."]
    address = " ".join(sys.argv[1:])
    
else:
    address = pyperclip.paste()
    
webbrowser.open("https://www.google.com/maps/place/" + address)