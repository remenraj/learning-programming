from array import *


# 1. Create an array and traverse.
print("Step 1")
my_array = array("i", [1, 2, 3, 4, 5])

# time complexity: O(n)
for i in my_array:
    print(i)


# 2. Access individual elements through indexes
print("Step 2")
print(my_array[0])
print(my_array[1])
print(my_array[2])
print(my_array[-1])  # prints the last element in the array


# 3. Append any value to the array using append() method
print("Step 3")
# by using append() method, we can only add an element to the end of an array
my_array.append(6)
print(my_array)

# 4. Insert value in an array using insert() method
# insert(index, value)
print("Step 4")
my_array.insert(0, 11)  # time complexity: O(n)
print(my_array)


# 5. Extend python array using extend() method
print("Step 5")
# by using extend() method, an array can be extended by more than one value
my_array1 = array("i", [10, 11, 12])

my_array.extend(my_array1)
print(my_array)


# 6. Add items from list into array using fromlist() method
print("Step 6")
temp_list = [20, 21, 22]

my_array.fromlist(temp_list)
print(my_array)


# 7. Remove any array element using remove() method
print("Step 7")
# remove(value) method removes the value from an array
my_array.remove(22)
print(my_array)


# 8. Remove last array element using pop() method
print("Step 8")
# pop(index)
my_array.pop()  # default value of index is -1
print(my_array)


# 9. Fetch any element through its index using index() method
print("Step 9")
# prints the index of the value 10
print(my_array.index(10))


# 10. Reverse a python array using reverse() method
print("Step 10")

my_array.reverse()
print(my_array)


# 11. Get array buffer information through buffer_info() method
print("Step 11")
# buffer_info() returns a tuple, which contains the memory address and the length of the buffer 
# that holds the array's contents in the form (address, length).
# prints the array starts from that point and the total number of elements in a tuple
print(my_array.buffer_info())


# 12. Check for number of occurrences of an element using count() method
print("Step 12")
# prints the number of times an element appears in the array
print(my_array.count(11))

# 13. Convert array to string using tostring() method
print("Step 13")
# tostring() is replaced by tobytes() in Python 3.2
temp_string = my_array.tobytes()
print(temp_string)

# converting back into integer array
# creating an empty array
int_array = array("i")
int_array.frombytes(temp_string)
print(int_array)


# 14. Convert array to a python list with same elements using tolist() method
print("Step 14")
temp_list = my_array.tolist()
print(temp_list)


# 15. Append a string to char array using fromstring() method
print("Step 15")

char_array = array("b") # typecode: b is unsigned char
char_array.frombytes(temp_string)
print(char_array)


# 16. Slice Elements from an array
print("Step 16")

print(my_array[:3])
print(my_array[1:4])
print(my_array[5:])