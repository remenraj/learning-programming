# Strong Password Detection, Automate the boring stuff on python, page number: 186

# Write a function that uses regular expressions to make sure the password string it is passed is strong. 
# A strong password is defined as one that is at least eight characters long, 
# contains both uppercase and lowercase characters, has at least one digit, and at least one special character.
# You may need to test the string against multiple regex patterns to validate its strength.

import re

def check_strong_password(password: str) -> bool:
    """
    This function takes a string of text and returns a boolean value.
    """
    strong_password_regex = re.compile(
        r"""
            ^   # start of string
            (?=.*[A-Z]) # at least one uppercase letter
            (?=.*[a-z]) # at least one lowercase letter
            (?=.*\d)    # at least one digit
            (?=.*?[#?!@$%^&*-]) # at least one special character
            .{8,}   # at least 8 characters
            $   # end of string
        """,
        re.VERBOSE,
    )
    
    return strong_password_regex.match(password) is not None


if __name__ == "__main__":
    print(check_strong_password("Abcde#f3gh"))
