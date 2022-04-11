# List operations/Functions


# + operator: concatenate lists
a = [1, 2, 3]
b = [4, 5, 6]

c = a + b
print(c)


# * operator: repeat list
a = [0]
a = a * 4
print(a)
b = [0, 1, 2, "x, y"]
print(b * 3)


# len() function: returns the length of the list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(a))


# max() function: returns the maximum value in the list
print(max(a))

# min() function: returns the minimum value in the list
print(min(a))


# sum() function: returns the sum of all the elements in the list
print(sum(a))

average = sum(a) / len(a)
print(f"Average is {average}")

# sort() function: returns a sorted list
a = [56, 48, 99, 100, 1000, 2, 3, 34, 5, 65, 7, 8, 99, 10]
print(a)
a.sort()
print(a)
