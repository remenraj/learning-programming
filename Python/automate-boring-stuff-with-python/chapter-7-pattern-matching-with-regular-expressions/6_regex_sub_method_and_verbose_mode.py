# The sub() regex method will substitute matches with some other text.
# Using \1, \2 and so will substitute group 1, 2, etc in the regex pattern.
# Passing re.VERBOSE lets you add whitespace and comments to the regex string passed to re.compile().
# If you want to pass multiple arguments (re.DOTALL , re.IGNORECASE, re.VERBOSE), combine them with the | bitwise operator.


import re

# ----------------------------------------------------------------------------------------------------------------------
# sub() method: substitute matches with some other text. ie, find and replace
names_regex = re.compile(r"Agent \w+")

mo = names_regex.findall("Agent Alice gave the secret documents to Agent Bob.")
print(mo)

# The sub() method will substitute matches with some other text.
so = names_regex.sub("REDACTED", "Agent Alice gave the secret documents to Agent Bob.")
print(so)

# adding pattern to the sub() method
# \1 will substitute group 1, \2 will substitute group 2, etc
names_regex = re.compile(r"Agent (\w)\w*")
so = names_regex.sub(
    r"Agent \1****", "Agent Alice gave the secret documents to Agent Bob."
)
print(so)

# Verbose Mode with re.VERBOSE
# In verbose mode, you can add whitespace and comments to the regex string passed to re.compile().
phone_num_regex = re.compile(
    r"""
    (\d\d\d-)|  # area code (optional) with dash
    (\(\d\d\d\))  # or area code with parens and no dash
    \d\d\d  # first 3 digits
    -   # second dash
    \d\d\d\d   # last 4 digits
    \sx\d{2,4}  # extension (optional) like x1234
    """,
    re.VERBOSE,
)
mo = phone_num_regex.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(mo)


# re.DOTALL: The re.DOTALL flag makes the re.compile() method treat a regular expression as a "multiline" pattern.
phone_num_regex = re.compile(
    r"""
    (\d\d\d-)|  # area code (optional) with dash
    (\(\d\d\d\))  # or area code with parens and no dash
    \d\d\d  # first 3 digits
    -   # second dash
    \d\d\d\d   # last 4 digits
    \sx\d{2,4}  # extension (optional) like x1234
    """,
    re.VERBOSE | re.DOTALL | re.IGNORECASE, # | bitwise operator, combines multiple flags
)

