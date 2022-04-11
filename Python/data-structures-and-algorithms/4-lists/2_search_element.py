# search for an element in the list
# time complexity: O(n)
# space complexity: O(1)
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# by using 'in' operator
if 20 in my_list:
    print(my_list.index(20))
else:
    print("Value not found")
    
    
# using linear search
# time complexity: O(n)
# space complexity: O(1)
def search_in_list(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return "Value not found"

print(search_in_list(my_list, 80))