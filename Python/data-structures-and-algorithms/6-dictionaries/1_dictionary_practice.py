# Dictionary operations
# Dictionary is an unordered collection of key-value pairs

# Dictionary                                vs          List

# Unordered                                             Ordered
# Access via keys                                       Access via index
# Collection of key-value pairs                         Collection of elements
# Preferred when you have unique key values             Preferred when you have ordered data
# No duplicate keys/members                             Allow duplicate members



# <--accessing element in dictionary----------------------------------------------------------------------------------------------->

# creating a dictionary
# time complexity: O(len(dict))
# space complexity: O(n)
my_dict = dict()
print(my_dict)

my_dict = {}
print(my_dict)

eng_to_sp = {"one": "uno", "two": "dos", "three": "tres"}
print(eng_to_sp)

# accessing a value 
# time complexity: O(1)
# space complexity: O(1)
print(eng_to_sp["two"])  


# <--insert/update an element in dictionary----------------------------------------------------------------------------------------------->

# update an element in dictionary
# time complexity: O(1)/amortized O(n)
# space complexity: O(1)
my_dict = {"name": "John", "age": 30}
print(my_dict)
my_dict["age"] = 31
print(my_dict)

# adding an element in dictionary
# time complexity: O(1)
# space complexity: amortized O(1)
my_dict["address"] = "London"
print(my_dict)

# <--traverse through dictionary----------------------------------------------------------------------------------------------->

# time complexity: O(n)
# space complexity: O(1)
def traverse_dict(dict):
    """Traverse through dictionary"""
    for key, value in dict.items():
        print(key, value)

    # # another method
    # for key in dict:
    #     print(key, dict[key])


traverse_dict(my_dict)

# <--search an element in dictionary----------------------------------------------------------------------------------------------->

# time complexity: O(n)
# space complexity: O(1)
def search_dict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value

    return "The value does not exist"


print(search_dict(my_dict, 27))
print(search_dict(my_dict, "John"))


# <--Delete an element in dictionary----------------------------------------------------------------------------------------------->

# time complexity: O(1)
# space complexity: O(1)
my_dict = {"name": "John", "age": 30, "address": "London", "phone": "123456789"}
print(my_dict)

# pop() method: pop(key) method removes the element with the specified key and returns the value of the element
# syntax: dictionary.pop(key, default_value)
# if key is not specified and default_value is given, then the method returns default_value
# if key is not specified and default_value is not specified, then the method returns None
# time complexity: O(1)/ amortized O(n)
# space complexity: O(1)
print(my_dict.pop("phone"))
print(my_dict)

# popitem() method: popitem() method removes the last inserted element and returns it
print(my_dict.popitem())
print(my_dict)

# clear() method: clear() method removes all the elements from the dictionary and returns None
# syntax: dictionary.clear()
print(my_dict.clear())
print(my_dict)

my_dict = {"name": "John", "age": 30, "address": "London", "phone": "123456789"}
print(my_dict)

# del keyword: del keyword removes the element with the specified key
del my_dict["address"]
print(my_dict)

# deleting a dictionary completely
del my_dict
# print(my_dict)    # NameError: name 'my_dict' is not defined
