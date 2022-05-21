# The regex method findall() is passed a string, and returns all matches in it, not just the first match.
# If the regex has 0 or 1 group, findall() returns a list of strings.
# If the regex has 2 or more groups, findall() returns a list of tuples of strings.
# \d is a shorthand character class that matches digits. \w matches "word characters" (letters, numbers, and the underscore). \s matches whitespace characters (space, tab, newline).
# The uppercase shorthand character classes \D, \W, and \S match characters that are not digits, word characters, and whitespace.
# You can make your own character classes with square brackets: [aeiou]
# A ^ caret makes it a negative character class, matching anything not in the brackets: [^aeiou]


import re

phone_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
# findall() returns a list of all matches
mo = phone_regex.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(mo)

phone_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
# findall() with groups returns a list of tuples
mo = phone_regex.findall("Cell: 415-555-9999 Work: 212-555-0000 Office: 555-9999")
print(mo)

# here we use the groups() method to extract the parts of the match and the whole number including -
phone_regex = re.compile(r"((\d\d\d)-(\d\d\d-\d\d\d\d))")
mo = phone_regex.findall("Cell: 415-555-9999 Work: 212-555-0000 Office: 555-9999")
print(mo)

########################################################################################################################
# character classes

# christmas song example
lyrics = "12 drummers drumming, 11 pipers piping, 10 lords a-leaping, 9 ladies dancing, 8 maids a-milking, 7 swans a-swimming, 6 geese a-laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree"

# using re to find all instances of number followed by space and a word
xmas_regex = re.compile(r"\d+\s+\w+")
mo = xmas_regex.findall(lyrics)
print(mo)

# to match any vowel, use [aeiouAEIOU]
vowel_regex = re.compile(
    r"[aeiouAEIOU]"
)  # [aeiouAEIOU] is a character class == r"(a|e|i|o|u|A|E|I|O|U)"
mo = vowel_regex.findall("Robocop eats baby food. BABY FOOD.")
print(mo)

# matching two vowels in a row
vowel_regex = re.compile(r"[aeiouAEIOU]{2}")
mo = vowel_regex.findall("Robocop eats baby food. BABY FOOD.")
print(mo)

# to match any small letters, use [a-z]
small_letter_regex = re.compile(r"[a-z]")

# Negative character class
# to match any consonant, use [^aeiouAEIOU]
consonant_regex = re.compile(r"[^aeiouAEIOU]")
mo = consonant_regex.findall("Robocop eats baby food. BABY FOOD.")
print(mo)
