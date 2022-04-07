#! /usr/bin/env python3

# Chapter 6: Manipulating Strings, Page Number: 154
# Write a function named printTable() that takes a list of lists of strings
# and displays it in a well-organized table with each column right-justified.


def printTable(data):

    # finding the length of longest string in the list and right justifying with respect to that length
    for column in data:
        len_string = 0
        for item in column:
            if len(item) > len_string:
                len_string = len(item)

        # right justifying items with respect to the highest length of string in that particular list
        for i in range(len(column)):
            column[i] = column[i].rjust(len_string + 1, " ")
            # if you use (len_string, " ") above, you have to add space while printing it

    # printing the table
    for i in range(len(data[0])):
        for j in range(len(data)):
            print(data[j][i], end="")
        # adding a new line
        print()


if __name__ == "__main__":

    tableData = [
        ["apples", "oranges", "cherries", "banana"],
        ["Alice", "Bob", "Carol", "David"],
        ["dogs", "cats", "moose", "goose"],
    ]
    printTable(tableData)
