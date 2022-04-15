# Dictionary operations

# <--in operator------------------------------------------------------------------------------------------------------------------->

# in operator: in operator returns True if the specified key is present in the dictionary, otherwise False
# time complexity: O(1)
my_dict = {
    "one": "uno",
    "two": "dos",
    "three": "tres",
    "four": "cuatro",
    "five": "cinco",
}

# search for a key
print("one" in my_dict)
# search for a value
print("uno" in my_dict.values())


# <--for operator------------------------------------------------------------------------------------------------------------------->

# for operator: iterates over the keys of the dictionary
# time complexity: O(n)
for key in my_dict:
    print(key, my_dict[key])

