# Strings and Lists


# converting string to list
a = "spam spam spam"
b = list(a)
print(b)


# split() method: splits a string into a list
# default is "space"
b = a.split()
print(b)

a = "spam-spam1-spam2"
delimiter = "-"
b = a.split(delimiter)
print(b)

# joint() method: joins a list into a string
a = ["spam", "spam", "spam"]
delimiter = "="
b = delimiter.join(a)
print(b)
