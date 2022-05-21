#! /usr/bin/env python3
# program to scrape phone numbers and email addresses from clipboard text and paste them into the clipboard
import re, pyperclip


# Create a regex for phone numbers
phone_regex = re.compile(
    r"""
                         
# 415-555-0000, 555-0000, (415) 555-0000, ,555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?    # area code (optional)

(\s|-)                      # first separator

\d\d\d                      # first 3 digits

-                           # second separator

\d\d\d\d                    # last 4 digits

(((ext(\.)?\s)|x)           # extension word part (optional)

 (\d{2,5}))?                # extension digit part (optional)
)
""",
    re.VERBOSE,
)


# Create a regex for email addresses
email_regex = re.compile(
    r"""
                         
# something@something.com, something.something@something.com, something.something+something@something.com
# something.+something@something.something

[a-zA-Z0-9._%+-]+    # name part

@               # @ symbol

[a-zA-Z0-9.+_-]+    # domain name part
                   
(\.[a-zA-Z]{2,4})   # dot-something
)                     
""",
    re.VERBOSE,
)


# Get the text off the clipboard
text = pyperclip.paste()


# Extract the email/phone from this text
extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)


all_phone_numbers = []

for phone_number in extracted_phone:
    all_phone_numbers.append(phone_number[0])

# print(all_phone_numbers)
# print(extracted_email)


# Copy the extracted email/phone to the clipboard

# converting the list into a string with phone numbers/email separated by newlines
results = "\n".join(all_phone_numbers) + "\n" + "\n".join(extracted_email)

pyperclip.copy(results)
