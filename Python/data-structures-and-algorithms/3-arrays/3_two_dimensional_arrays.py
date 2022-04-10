# Two dimensional arrays

import numpy as np


# <--creating a two dimensional array----------------------------------------------------------------------------------------------->

# Day 1: 11, 15, 10, 6
# Day 2: 10, 14, 11, 5
# Day 3: 12, 17, 12, 8
# Day 4: 15, 18, 14, 9

#
# time complexity: O(1)
# space complexity: O(mn)
two_d_array = np.array(
    [[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]
)
print(two_d_array)
print(type(two_d_array))  # type of array: 'numpy.ndarray' or 'np.ndarray'

print(len(two_d_array))  # number of rows
print(len(two_d_array[0]))  # number of columns

# <--inserting a new row and column-------------------------------------------------------------------------------------------->

#
# time complexity: O(mn)
# space complexity: O(1)
# obj=index/position of the row/column to be inserted, axis= 0 for row and 1 for column

# adding a new column
new_two_d_array = np.insert(arr=two_d_array, obj=0, values=[[1, 2, 3, 4]], axis=1)
print(new_two_d_array)
# adding a new row
new_two_d_array = np.insert(arr=two_d_array, obj=0, values=[[1, 2, 3, 4]], axis=0)
print(new_two_d_array)

# adding row at the end of the two dimensional array
# time complexity: O(1)
# space complexity: O(1)
new_two_d_array = np.append(
    arr=two_d_array, values=[[1, 2, 3, 4]], axis=0
)  # adding new row
print(new_two_d_array)


# <--accessing an element of two dimensional array----------------------------------------------------------------------------------------------->

# element a[i][j] where i = row index, j = column index
# time complexity: O(1)
# space complexity: O(1)
def access_elements(array: np.ndarray, row_index: int, column_index: int) -> None:
    """Prints the element in an array"""
    if row_index > len(array) or column_index > len(array[0]):
        print("Incorrect index")
    else:
        print(array[row_index][column_index])


print(two_d_array)
access_elements(array=two_d_array, row_index=2, column_index=3)


# <--traverse a two dimensional array----------------------------------------------------------------------------------------------->

# time complexity: O(mn)
# space complexity: O(1)
def traverse_two_d_array(array: np.ndarray) -> None:
    """Traverse an array"""

    for i in range(len(array)):  # looping through rows  O(mn)
        for j in range(len(array[0])):  # looping through columns   O(n)
            print(array[i][j])  # O(1)


traverse_two_d_array(array=two_d_array)


# <--searching for an element in two dimensional array----------------------------------------------------------------------------------------------->

# linear search
# time complexity: O(mn)
# space complexity: O(1)
def search_two_d_array(array: np.ndarray, value: int) -> str:
    """Search for an element in an array using linear search"""

    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return f"The value is found at index: row={i} column={j}"

    return "Value not found"


print(search_two_d_array(array=two_d_array, value=10))


# <--deletion of row/column in two dimensional array----------------------------------------------------------------------------------------------->

print(two_d_array)
# obj=index/position of the row/column to be inserted, axis= 0 for row and 1 for column

# time complexity: O(mn)
# space complexity: O(1)
# when deleting last row/column, time complexity: O(1)
# deleting first row
new_two_d_array = np.delete(arr=two_d_array, obj=0, axis=0)
print(new_two_d_array)
# deleting first column
new_two_d_array = np.delete(arr=two_d_array, obj=0, axis=1)
print(new_two_d_array)
