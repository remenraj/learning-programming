# Chapter 8: Input validation, page number: 187
# Input validation code checks that values entered by the user, such as text from the input() function,
# are formatted correctly.
# https://pyinputplus.readthedocs.io/

import pyinputplus as pyip

# inputStr() Is like the built-in input() function but has the general PyInputPlus features.
# You can also pass a custom validation function to it

# inputNum(): Ensures the user enters a number and returns an int or float,
# depending on if the number has a decimal point in it

# inputChoice(): Ensures the user enters one of the provided choices
# inputMenu(): Is similar to inputChoice(), but provides a menu with numbered or lettered options

# inputDatetime(): Ensures the user enters a date and time
# inputYesNo(): Ensures the user enters a “yes” or “no” response
# inputBool(): Is similar to inputYesNo(), but takes a “True” or “False” response and returns a Boolean value

# inputEmail(): Ensures the user enters a valid email address
# inputFilepath(): Ensures the user enters a valid file path and filename, and can optionally check that a file with that name exists

# inputPassword() Is like the built-in input(), but displays * characters as the user types so that passwords,
# or other sensitive information, aren’t displayed on the screen

response = pyip.inputInt(prompt="Enter a Number: ")  # Ask the user to enter a number
print(response)


response = pyip.inputNum("Enter a number >= 4: ", min=4)    # Ask the user to enter a number, and ensure it is greater than or equal to 4
print(response)


response = pyip.inputNum("Enter num > 4: ", greaterThan=4)  # Ask the user to enter a number, and ensure it is greater than 4
print(response)


response = pyip.inputNum(">", min=4, lessThan=6)    # Ask the user to enter a number, and ensure it is greater than 4 and less than 6
print(response)


# The blank Keyword Argument: By default, blank input isn’t allowed unless the blank keyword argument is set to True.
response = pyip.inputNum('Enter num, try black input: ', blank=True)
print(response)


# The limit, timeout, and default Keyword Arguments
# By default, the PyInputPlus functions will continue to ask the user for valid input forever (or for as long as the program runs). 
# If you’d like a function to stop asking the user for input after a certain number of tries or a certain
# amount of time, you can use the limit and timeout keyword arguments.

response = pyip.inputNum(limit=2)
response = pyip.inputNum(timeout=10)

response = pyip.inputNum(limit=2, default='N/A')    # If the user doesn’t enter a number, the default value will be returned
print(response)

