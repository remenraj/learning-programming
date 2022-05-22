# How to keep an idiot busy for hours
# Automate the boring stuff with Python, page number: 194

import pyinputplus as pyip

def idiot():
    while True:
        response = pyip.inputYesNo(prompt="Want to know how to keep an idiot busy for hours?: ")
        if response == 'no':
            break

    print('Thank you. Have a nice day.')
    
    
if __name__ == "__main_no_":
    idiot()