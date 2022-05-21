# ^ means the string must start with pattern, $ means the string must end with the pattern. Both means the entire string must match the entire pattern.
# The . dot is a wildcard; it matches any character except newlines.
# Pass re.DOTALL as the second argument to re.compile() to make the . dot match newlines as well.
# Pass re.I as the second argument to re.compile() to make the matching case-insensitive.

import re

# regex to match string starting with the word "Hello"
begin_with_hello_regex = re.compile(r"^Hello")
mo = begin_with_hello_regex.search("Hello world!")
print(mo.group())

mo = begin_with_hello_regex.search("He is not him. Hello world!")
# print(mo.group()) # this will raise an error because here mo == None

# regex to match string ending with the word "world!"
# $ means the string must end with the pattern
end_with_world_regex = re.compile(r"world!$")

mo = end_with_world_regex.search("Hello world!")
print(mo.group())

# regex to match string of numbers, beginning and ending with a number.
all_digits_regex = re.compile(r"^\d+$")
mo = all_digits_regex.search("12345")
print(mo.group())

mo = all_digits_regex.search("12345abcdefgh3343")
# print(mo.group()) # this will raise an error because here mo == None

# . matches any character except newlines
at_regex = re.compile(r".at")
mo = at_regex.findall("The cat in the hat sat on the flat mat.")  # flat will not match
print(mo)

# one or two characters preceded by at
at_regex = re.compile(r".{1,2}at")
mo = at_regex.findall(
    "The cat in the hat sat on the flat mat."
)  # here flat will be found and also " cat" because it is one or two characters
print(mo)

# .* matches anything except newlines and the dot is a wildcard. It matches in greedy mode
name_regex = re.compile(r"First Name: (.*) Last Name: (.*)")

mo = name_regex.findall("First Name: Al Last Name: Sweigart")
print(mo)


# .*? matches anything except newlines and the dot is a wildcard. It matches in non-greedy mode
serve = "<To serve humans> for dinner.>"

greedy_regex = re.compile(r"<.*>")
mo = greedy_regex.findall(serve)
print(mo)

non_greedy_regex = re.compile(r"<(.*?)>")
mo = non_greedy_regex.findall(serve)
print(mo)

########################################################################################################################
# new line character \n
prime = "Serve the public trust.\nProtect the innocent.\nUphold the law."
dot_star_regex = re.compile(r".*")

mo = dot_star_regex.search(prime)
print(mo.group())

dot_star_regex = re.compile(
    r".*", re.DOTALL
)  # this will make the . dot match newlines as well
mo = dot_star_regex.search(prime)
print(mo.group())


########################################################################################################################
# Case insensitive

# here only small letters will be matched
vowel_regex = re.compile(r"[aeiou]")
mo = vowel_regex.findall("RoboCop eats baby food. BABY FOOD.")
print(mo)

# here regex is case insensitive by using re.I or re.IGNORECASE
vowel_regex = re.compile(r"[aeiou]", re.I)
mo = vowel_regex.findall("RoboCop eats baby food. BABY FOOD.")
print(mo)
