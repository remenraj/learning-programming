# Function to check if a number is odd in a list of numbers and return True if so

# recursive function
def someRecursive(lst, check_odd):

    assert type(lst) == list and type[lst[0]] == int, "It must be a list of integers"

    # base case
    if len(lst) == 0:
        return False

    # recursive case
    if not check_odd(lst[0]):
        return someRecursive(lst[1:], check_odd=isOdd)
    else:
        return True


def isOdd(num):
    """Check if a number is odd and return True if so"""

    if num % 2 == 1:
        return True
    else:
        return False


if __name__ == "__main__":

    print(someRecursive([1, 2, 3, 4], isOdd))  # true
    print(someRecursive([4, 6, 8, 9], isOdd))  # true
    print(someRecursive([4, 6, 8], isOdd))  # false
