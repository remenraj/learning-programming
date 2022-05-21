# Regular expressions are mini-language for specifying text patterns. Writing code to do pattern matching without regular expressions is a huge pain.
# Regex strings often use backslashes (like \d), so they are often written using raw strings: r'\d'
# \d is the regex for a numeric digit character.
# Import the re module first.
# Call the re.compile() function to create a regex object.
# Call the regex object's search() method to create a match object.
# Call the match object's group() method to get the matched string.


import re

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."

# \d = digit
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

# search() returns the first match and creates a Match object
matched_object = phoneNumRegex.search(message)
print(matched_object)

# prints the first occurrence of the matched  string in Match object
print(matched_object.group())

# findall() returns a list of all matches
matched_object = phoneNumRegex.findall(message)
print(matched_object)
