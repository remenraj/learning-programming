# Chapter 4: Lists, Page Number: 107
# A program that takes a list value as an argument
# and returns a string with all the items separated by a comma and a space,
# with 'and' inserted before the last item.


def comma_code_1(the_list):
    """
    Takes a list value as an argument and returns a string with all the items
    separated by a comma and a space, with 'and' inserted before the last item.
    """

    length_of_list = len(the_list)

    # check if the list is empty
    if length_of_list == 0:
        return ""

    # check if the list has only one item
    if length_of_list == 1:
        return the_list[0]

    # check if the list has two items
    if length_of_list == 2:
        return the_list[0] + " and " + the_list[1]

    # check if the list has more than two items
    if length_of_list > 2:

        converted_string = ""

        for n in range(length_of_list):

            converted_string += the_list[n]

            if n == length_of_list - 2:
                converted_string += " and "

            if n < length_of_list - 2:
                converted_string += ", "

        return converted_string


def comma_code_2(lst):
    """
    Takes a list value as an argument and returns a string with all the items
    separated by a comma and a space, with 'and' inserted before the last item.
    """
    # Check if the list is empty
    if not lst:
        return ""

    # Check if the list has only one item
    if len(lst) == 1:
        return str(lst[0])

    # Check if the list has more than one item
    if len(lst) > 1:
        # Get the last item of the list
        last_item = lst[-1]
        # Remove the last item from the list
        lst.pop()
        # Join all the items in the list with a comma and a space
        string = ", ".join(lst)
        # Add 'and' before the last item
        string += " and " + last_item
        return string


if __name__ == "__main__":

    list_to_be_converted = ["apples", "bananas", "tofu", "cats"]

    print(comma_code_1(list_to_be_converted))
    print(comma_code_2(list_to_be_converted))
