# Regex Version of the strip() Method, Automate the boring stuff on python, page number: 186

# Write a function that takes a string and does the same thing as the strip() string method.
# If no other arguments are passed other than the string to strip,
# then whitespace characters will be removed from the beginning and end of the string.
# Otherwise, the characters specified in the second argument to the function will be removed from the string.

import re


def regex_strip(text: str, chars: str = "") -> str:
    """
    This function takes a string and returns a string with the characters specified in the second argument to the function removed from the beginning and end of the string.
    """
    if chars == "":
        return re.sub(
            r"^\s+|\s+$", "", text
        )  # remove whitespace from beginning and end of string
    else:
        return re.sub(
            r"^[" + chars + "]+|[" + chars + "]+$", "", text
        )  # remove specified characters from beginning and end of string


if __name__ == "__main__":
    print(regex_strip("   Hello World!  ")) # strips whitespace from beginning and end of string
    print(regex_strip("Hello World!  ")) # strips whitespace from end of string
    print(regex_strip("   Hello World!")) # strips whitespace from beginning of string
    
    print(regex_strip("Hello World!", "Hello")) # strips Hello from beginning and end of string
    print(regex_strip("Hello World!", "!")) # strips ! from beginning and end of string
    