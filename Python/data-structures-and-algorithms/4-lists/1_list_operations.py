# <--accessing element in list----------------------------------------------------------------------------------------------->

# time complexity: O(1)
# space complexity: O(1)
shopping_list = ["milk", "cheese", "butter"]    # creating a list, space complexity: O(n)
print(shopping_list[2])
print(shopping_list[-1])


# <--traversing the list----------------------------------------------------------------------------------------------------->

# time complexity: O(n)
# space complexity: O(1)
for i in range(len(shopping_list)):
    shopping_list[i] = shopping_list[i] + "!"
    print(shopping_list[i])


# <--update an element in list------------------------------------------------------------------------------------------------->

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)

# updating an element in the list
# time complexity: O(1)
# space complexity: O(1)
my_list[2] = "hello"


# <--insert an element in list------------------------------------------------------------------------------------------------->

# using insert() method: insert(index, element)
print(my_list)
# time complexity: O(n)
# space complexity: O(1)
my_list.insert(3, "world")
print(my_list)

# using append() method: append(element)
print(my_list)
# time complexity: O(1)
# space complexity: O(1)
my_list.append("!")
print(my_list)

# using extend() method: extend(list)
print(my_list)
new_list = [11, 12, 13, 14, 15]
print(new_list)
# time complexity: O(n), since it is looping through the list
# space complexity: O(1)
my_list.extend(new_list)
print(my_list)


# <--slicing in list------------------------------------------------------------------------------------------------->

print(my_list)
print(my_list[0:2])  # printing first two elements
print(my_list[:4])  # printing first four elements)
print(my_list[2:])  # printing from index 2 to the end
print(my_list[:])  # printing all elements

# replacing first two elements with new list
my_list[:2] = ["x", "y"]
print(my_list)

# <--deleting an element in list----------------------------------------------------------------------------------------------->

# pop() method: pop(index)
# time complexity: O(1)/O(n)
# space complexity: O(1)
print(my_list)
print(
    my_list.pop()
)  # deleting last element by default an d prints the element that is deleted, time complexity: O(1)
print(my_list)
my_list.pop(1)  # deleting element at index 1, time complexity: O(n)
print(my_list)


# delete() method: delete(index)
# time complexity: O(1)/O(n)
# space complexity: O(1)
del my_list[4]  # deleting element at index 1
print(my_list)
del my_list[3:5]  # deleting elements from index 3 to index 5
print(my_list)


# remove() method: remove(element)
# time complexity: O(1)/O(n)
# space complexity: O(1)
my_list.remove("x")  # deleting element "x"
print(my_list)
