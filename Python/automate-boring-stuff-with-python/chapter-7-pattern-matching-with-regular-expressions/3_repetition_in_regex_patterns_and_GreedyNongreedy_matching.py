# The ? says the group matches zero or one times.
# The * says the group matches zero or more times.
# The + says the group matches one or more times.
# The curly braces can match a specific number of times.
# The curly braces with two numbers matches a minimum and maximum number of times.
# Leaving out the first or second number in the curly braces says there is no minimum or maximum.
# "Greedy matching" matches the longest string possible, "nongreedy matching" (or "lazy matching") matches the shortest string possible.
# Putting a question mark after the curly braces makes it do a nongreedy/lazy match.


import re


########################################################################################################################
# ? matches zero or one times
bat_regex = re.compile(r"Bat(wo)?man")

mo = bat_regex.search("The adventures of Batman")
print(mo.group())

mo = bat_regex.search(
    "The adventures of Batwoman"
)  # this doesn't match Batwowowoman because ? matches zero or one times
print(mo.group())

mo = bat_regex.findall("The adventures of Batman and Batwoman")
print(mo)


# searching for optional groups like number with or without area codes
phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")  # requires area code

mo = phone_num_regex.search("Cell: 555-9999 Work: 555-0000")
# print(mo.group())   # will return error because mo == None

phone_num_regex = re.compile(
    r"(\d\d\d-)?\d\d\d-\d\d\d\d"
)  # optional/area code can appear once or zero times

mo = phone_num_regex.search("Cell: 454-555-9999")
print(mo.group())
mo = phone_num_regex.search("Work: 555-0000")
print(mo.group())

########################################################################################################################
# * matches zero or more times
bat_regex = re.compile(r"Bat(wo)*man")

mo = bat_regex.search("The adventures of Batman")
print(mo.group())

mo = bat_regex.search("The adventures of Batwoman")
print(mo.group())

mo = bat_regex.search("The adventures of Batwowoman")
print(mo.group())


########################################################################################################################
# + matches one or more times

bat_regex = re.compile(r"Bat(wo)+man")

mo = bat_regex.search("The adventures of Batman")
# print(mo.group())   # returns an error, since mo == None

mo = bat_regex.search("The adventures of Batwoman")
print(mo.group())

mo = bat_regex.search("The adventures of Batwowoman")
print(mo.group())


########################################################################################################################
# escaping characters
regex = re.compile(r"\+\*\?")

mo = regex.search("I learned about +*? regex syntax.")
print(mo.group())

regex = re.compile(r"(\+\*\?)+")

mo = regex.search("I learned about +*?+*?+*?+*?+*? regex syntax.")
print(mo.group())


########################################################################################################################
# matching exactly 3 times
ha_regex = re.compile(r"(Ha){3}")

mo = ha_regex.search("HaHaHa")
print(mo.group())


# searching for 3 phone numbers in a row that may or maynot have area codes and separated by comma
phone_num_regex = re.compile(r"((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}")

mo = phone_num_regex.search("Cell: 555-9999,998-555-0000,555-9999")
print(mo.group())

# searching for at least or at most patterns
ha_regex = re.compile(r"(Ha){3,5}")
# ha_regex = re.compile(r"(Ha){,5}")  # at most 5
# ha_regex = re.compile(r"(Ha){3,}")  # at least 3


mo = ha_regex.search("HaHaHaHaHa")
print(mo.group())

mo = ha_regex.search("HaHaHa")
print(mo.group())

mo = ha_regex.search("HaHaHaHa")
print(mo.group())

mo = ha_regex.search("HaHaHaHaHaHaHaHaHaHaHaHa")    # by default it does greedy matches, so prints first 5 ha's
print(mo.group())

ha_regex = re.compile(r"(Ha){3,5}?")  # ? makes it do a non-greedy match
mo = ha_regex.search("HaHaHaHaHaHaHaHaHaHaHaHa")    # prints first 3 ha's if it has more than 3 ha's
print(mo.group())

