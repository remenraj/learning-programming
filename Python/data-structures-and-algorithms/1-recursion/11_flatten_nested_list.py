# Program to flatten nested list into a single list

# recursive function to flatten list
def flatten(the_list):

    assert type(the_list) is list, "the_list must be a list"

    flattened_list = []

    # iterate over the list
    for item in the_list:

        # if item is a list, then recursively call flatten()
        if type(item) is list:
            # extend adds the elements of the list to it while append adds the list as its next element
            flattened_list.extend(flatten(the_list=item))

        # if item is not a list, then append it to flattened_list
        else:
            flattened_list.append(item)

    # return flattened list
    return flattened_list


if __name__ == "__main__":

    print(flatten([1, 2, 3, [4, 5]]))  # [1, 2, 3, 4, 5]
    print(flatten([1, [2, [3, 4], [[5]]]]))  # [1, 2, 3, 4, 5]
    print(flatten([[1], [2], [3]]))  # [1, 2, 3]
    print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))  # [1, 2, 3]
