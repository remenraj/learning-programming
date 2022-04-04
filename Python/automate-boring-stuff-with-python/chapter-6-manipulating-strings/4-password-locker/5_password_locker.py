#! /usr/bin/env python3
# An Insecure Password Locker

import sys, pyperclip

# if pyperclip module not found, then install it through cmd by using the following command:
#  py -m pip install pyperclip
# -m pip is an option for Python that essentially means "find and run pip for me"

# py.exe is a global command on Windows (when installed) that will automatically select the latest version of Python. 
# It is like using C:\Users\username\AppData\Local\Programs\Python\Python37\python.exe 
# but without having to type it every time.


PASSWORDS = {
    "email": "F7minlBDDuvMJuxESSKHFhTxFtjVB6",
    "blog": "VmALvQyKAxiVH5G8v01if1MLZF3sdt",
    "luggage": "12345",
}

if len(sys.argv) < 2:
    print("Usage: python password_locker.py [account] - copy account password")
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)