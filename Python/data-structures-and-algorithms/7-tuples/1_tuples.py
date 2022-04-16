# A tuple is an immutable sequence of Python objects.
# Tuples are also comparable and hashable.
# Elements in a tuple cannot be modified.


# Tuples vs Lists
# List is mutable whereas tuple is immutable.
# Elements in a list can be modified whereas elements in a tuple cannot be modified.
# Item assignment in a tuple will raise TypeError.
# You can delete an entire tuple by using del keyword. But you cannot delete individual elements.
# Tuples can be stored in lists and vice versa.
# Both tuples and lists can be nested.


# We generally use tuples for fixed size data structures, heterogeneous data structures(different), and data that is not changeable.
# And lists for mutable data structures, homogeneous data structures(same), and data that is changeable.
# Iterating through a tuple is faster than iterating through a list.
# Typles that contain immutable elements can be used as a key for a dictionary.
# If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

# <--create a tuple----------------------------------------------------------------------------------------------->

# time complexity: O(1)
# space complexity: O(n)

new_tuple = ("a", "b", "c")
print(new_tuple)
print(type(new_tuple))

new_tuple = "a", "b", "c"
print(new_tuple)
print(type(new_tuple))

# tuple with one element
new_tuple = ("a",)
print(new_tuple)

# using tuple constructor: tuple()
new_tuple = tuple()
new_tuple1 = tuple("abcdefg")
print(new_tuple)
print(new_tuple1)


# <--access a tuple element----------------------------------------------------------------------------------------------->
# time complexity: O(1)
# space complexity: O(1)

# using bracket [] operator
new_tuple = ("a", "b", "c", "d", "e")

print(new_tuple[1])
print(new_tuple[-1])

# using slice [start:stop:step] operator
print(new_tuple[1:3])
print(new_tuple[1:])
print(new_tuple[:])


# <--traverse through tuple--------------------------------------------------------------------------------------------------------->
# time complexity: O(n)
# space complexity: O(1)

# using for loop
for i in new_tuple:
    print(i)

for i in range(len(new_tuple)):
    print(new_tuple[i])


# <--check if element exists in tuple----------------------------------------------------------------------------------------------->

# using in operator

if  "a" in new_tuple:
    print("a is in new_tuple")

print("a" in new_tuple)
print("f" in new_tuple)


# using linear search to return index of the element
# time complexity: O(n)
# space complexity: O(1)
def search_tuple(tuple_, element):
    for i in tuple_:
        if i == element:
            return tuple_.index(i)

    return "The element is not in the tuple"

print(search_tuple(new_tuple, "c"))
print(search_tuple(new_tuple, "f"))


# <--delete a tuple----------------------------------------------------------------------------------------------->

del new_tuple1
