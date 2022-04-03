# Program to find the product of a list of numbers using recursion

from numpy import number

# recursive function to find the product of a list of numbers
def productOfArray(number_list):

    assert type(number_list) == list, "It must be a list of numbers"

    # base case
    if len(number_list) == 0:
        return 1

    # recursive case
    return number_list[0] * productOfArray(number_list[1:])


# calling the main function
if __name__ == "__main__":
    print(productOfArray([1, 2, 3]))  # 6
    print(productOfArray([1, 2, 3, 10]))  # 60
