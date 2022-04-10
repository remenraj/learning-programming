from array import *

"""
When to use an array:
    * To store multiple variables of same data type
    * Random access
    
When to avoid using an array:
    * Same data type elements
    * Reserve memory
"""

# <------------------ Creating an array ------------------------>
# integer array
arr1 = array("i", [1, 2, 3, 4, 5])  # O(1)
print(arr1)

# double array
arr2 = array("d", [1.1, 2.2, 3.3, 4.4, 5.5])  # O(1)
print(arr2)


# <------------------ Inserting an element into an array ------------------------>

# inserting an element at the end of the array
# first argument is the index and second argument is the value
arr1.insert(5, 10)  # O(1)
print(arr1)

# inserting an element at the beginning of the arrray
arr1.insert(0, 0)  # O(n)
print(arr1)

# inserting an element at the index 2
arr1.insert(1, 10)  # O(n)
print(arr1)


#<------------------ Array traversal ------------------------>

def traverseArray(array):
    for i in array: # O(n)
        print(i)    # O(1)

# time complexity = O(n)
# space complexity = O(1)
traverseArray(arr1) 


#<------------------ Accessing an element in an array ------------------------>

def accessElement(array, index):
    """ Prints the element at the index """
    # try:
    #     print(array[index])
    # except IndexError:
    #     print("Incorrect Index")
    if index >= len(array):
        print("Incorrect Index")
    else:
        print(array[index])
        
# time complexity = O(1)
# space complexity = O(1)
accessElement(arr1, 1)


#<------------------ Finding an element to an array ------------------------>

def searchInArray(array, value):
    """Returns the index of the element if found"""
    for i in array: # O(n)
        if i == value:  # O(1)
            return array.index(value)   # O(1)
    return "The element does not exist in the array"    # O(1)

# time complexity = O(n)
# space complexity = O(1)
print(searchInArray(arr1, 10))

#<------------------ Deleting an element from an array ------------------------>

print(arr1)
# deleting an element from the middle of an array, it rearranges the array

# removes the first value found
arr1.remove(10) # O(n)
print(arr1)

# deleting an element from the end of an array
arr1.remove(10) # O(1)
print(arr1)

