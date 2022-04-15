# Dictionary methods

# <--clear()------------------------------------------------------------------------------------------------------------------->

my_dict = {"name": "John", "age": 30, "address": "London", "phone": "123456789"}
print(my_dict)

# clear() method: clear() method removes all the elements from the dictionary and returns None
# syntax: dictionary.clear()
print(my_dict.clear())
print(my_dict)


# <--copy()------------------------------------------------------------------------------------------------------------------->

# copy() method: copy() method returns a shallow copy of the dictionary
# syntax: dictionary.copy()
my_dict = {"name": "John", "age": 30, "address": "London", "phone": "123456789"}
print(my_dict)
new_dict = my_dict.copy()
print(new_dict)


# <--fromkeys()------------------------------------------------------------------------------------------------------------------->

# fromkeys() method: fromkeys() method returns a dictionary with the specified keys and values
# syntax: dict.fromkeys(sequence[], value)
# sequence: sequence of keys, and value: value to be assigned to the keys which is optional
new_dict = {}.fromkeys([1, 2, 3], 0)
print(new_dict)

# by default the value is None
new_dict = {}.fromkeys([1, 2, 3])
print(new_dict)

new_dict = my_dict.fromkeys(["name", "age"])
print(new_dict)


# <--get()------------------------------------------------------------------------------------------------------------------->

# get() method: get() method returns the value of the specified key
# syntax: # syntax: dictionary.get(key, default_value)
# key: key whose value is to be returned
# default_value: value to be returned if the key does not exist, if key is not specified and default_value is not specified,
# then the method returns None
print(my_dict)
print(my_dict.get("name", 27))

print(my_dict.get("city", "New York"))
print(my_dict.get("city"))


# <--items()------------------------------------------------------------------------------------------------------------------->

# items() method: items() method returns a list of tuples containing key-value pairs
# syntax: dictionary.items()

print(my_dict.items())
print(type(my_dict.items()))  # <class 'dict_items'>


# <--keys()------------------------------------------------------------------------------------------------------------------->

# keys() method: keys() method returns a list of all dictionary keys
# syntax: dictionary.keys()

print(my_dict.keys())
print(type(my_dict.keys()))  # <class 'dict_keys'>


# <--values()------------------------------------------------------------------------------------------------------------------->

# values() method: values() method returns a list of all dictionary values
# syntax: dictionary.values()
print(my_dict.values())


# <--popitem()------------------------------------------------------------------------------------------------------------------->

# popitem() method: popitem() method removes the last inserted element and returns it
# syntax: dictionary.popitem()

print(my_dict)
print(my_dict.popitem())
print(my_dict)


# <--setdefault()------------------------------------------------------------------------------------------------------------------->

# setdefault() method: setdefault() method returns the value of the specified key and inserts the key-value pair if the key does not exist
# if the key does not exist and default value is not specified, then the method returns None
# syntax: dictionary.setdefault(key, default_value)


print(my_dict)
print(my_dict.setdefault("name", "Alice"))

print(my_dict.setdefault("pet", "Alice"))
print(my_dict)


# <--pop()------------------------------------------------------------------------------------------------------------------->

# pop() method: pop(key) method removes the element with the specified key and returns the value of the element
# syntax: dictionary.pop(key)
# time complexity: O(1)/ amortized O(n)
# space complexity: O(1)
print(my_dict.pop("pet"))
print(my_dict)

print(my_dict.pop("vehicle", "Not found"))
print(my_dict)


# <--update()------------------------------------------------------------------------------------------------------------------->

# update() method: update() method updates the dictionary with another dictionary elements or from specified key-value pairs
# if the key already exists, then the value is updated
# if the key does not exist, then the key-value pair is inserted
# return from update() method is None
# update() method takes a dictionary or tuple as an argument
# syntax: dictionary.update(dict2)

print(my_dict)

new_dict = {"name": "Alice", "age": 27, "address": "Berlin"}

my_dict.update(new_dict)
print(my_dict)

new_dict = {"a": 1, "b": 2, "c": 3}
my_dict.update(new_dict)
print(my_dict)

my_dict.update((("d", 4), ("e", 5)))
print(my_dict)


# <--all() method------------------------------------------------------------------------------------------------------------------->

# all() method: returns True if all the values in the dictionary are True, otherwise False
# syntax: all(dict)
# cases:
# 1. all values are True: True
my_dict1 = {"one": True, "two": True, "three": True, "four": True, "five": True}
print(all(my_dict1))

# 2. all values are False: False
my_dict2 = {"one": False, "two": False, "three": False, "four": False, "five": False}
print(all(my_dict2))

# 3. some values are True and some are False: False
my_dict3 = {"one": True, "two": False, "three": True, "four": False, "five": True}
print(all(my_dict3))

# 4. all values are None: False
my_dict4 = {"one": None, "two": None, "three": None, "four": None, "five": None}
print(all(my_dict4))

# 5. empty iterable: True
my_dict5 = {}
print(all(my_dict5))


# <--any() method------------------------------------------------------------------------------------------------------------------->

# any() method: returns True if any of the values in the dictionary are True, otherwise False
# syntax: any(dict)
# cases:
# 1. all values are True: True
my_dict1 = {"one": True, "two": True, "three": True, "four": True, "five": True}
print(any(my_dict1))

# 2. all values are False: False
my_dict2 = {"one": False, "two": False, "three": False, "four": False, "five": False}
print(any(my_dict2))

# 3. some values are True and some are False: True
my_dict3 = {"one": True, "two": False, "three": True, "four": False, "five": True}
print(any(my_dict3))

# 4. all values are None: False
my_dict4 = {"one": None, "two": None, "three": None, "four": None, "five": None}
print(any(my_dict4))

# 5. empty iterable: False
my_dict5 = {}
print(any(my_dict5))


# <--len() method------------------------------------------------------------------------------------------------------------------->

# len() method: returns the length of the dictionary
print(my_dict)
print(len(my_dict))


# <--sorted() method------------------------------------------------------------------------------------------------------------------->

# sorted() method: returns a sorted list of the dictionary keys
# syntax: sorted(dict)/ sorted(iterable, key=None, reverse=False)
# iterable: iterable object: it maybe list, tuple, string, set, dictionary
# key: key function, it is a function that is used to extract a comparison key from an element
# reverse: reverse flag, True or False, default is False
# time complexity: O(n log n)
# space complexity: O(n)
#

# printing sorted keys
print(sorted(my_dict))
print(sorted(my_dict, key=None, reverse=True))

# printing sorted list of keys based on length of the key
print(sorted(my_dict, key=len))
print(my_dict)
