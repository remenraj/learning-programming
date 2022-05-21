# Groups are created in regex strings with parentheses.
# The first set of parentheses is group 1, the second is 2, and so on.
# Calling group() or group(0) returns the full matching string, group(1) returns group 1's matching string, and so on.
# Use \( and \) to match literal parentheses in the regex string.
# The | pipe can match one of many possible groups.


import re


########################################################################################################################
# regex groups
########################################################################################################################
phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

# match object
mo = phone_num_regex.search("Cell: 415-555-9999")
print(mo.group())

# findall() returns a list of all matches where each match is a string
mo = phone_num_regex.findall("Cell: 415-555-9999, work: 212-555-0000")
print(mo)

# parentheses are used to group, here there are two groups.
phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")

mo = phone_num_regex.search("Cell: 415-555-9999")
print(mo.group())
# prints the first group
print(mo.group(1))
# prints the second group
print(mo.group(2))

# to look for parenthesis in a string, use \
phone_num_regex = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
mo = phone_num_regex.search("My number is (415) 555-4242.")
print(mo.group())

# when using groups, findall() returns a list of tuples
phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phone_num_regex.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(mo)

########################################################################################################################
# | pipe character is used to group and pipe the groups together to create a single string
########################################################################################################################
bat_regex = re.compile(r"Bat(man|mobile|copter|bat|)")

mo = bat_regex.search("Batmobile lost a wheel")
print(mo.group())
mo = bat_regex.search("Batmotorcycle lost a wheel")
print(mo.group())
