# Tuple Operations/Functions

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
my_tuple1 = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")

# using + operator(concatenation)
print(my_tuple + my_tuple1)


# using * operator(repeating)
print(my_tuple * 3)

# using in operator(checking if element exists in tuple)
print(5 in my_tuple)


# count() method: returns the number of times the specified value appears in the tuple
print(my_tuple.count(2))

# index() method: returns the index of the first occurrence of the specified value
print(my_tuple.index(5))

# len() method: returns the length of the tuple
print(len(my_tuple))

# max() method: returns the largest item in the tuple
print(max(my_tuple))

# min() method: returns the smallest item in the tuple
print(min(my_tuple))

# tuple() method: returns a tuple from a sequence
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# converting list to tuple
print(tuple(my_list))