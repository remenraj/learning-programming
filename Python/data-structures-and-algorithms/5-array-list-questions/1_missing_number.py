# Find missing number in an integer array of 1 to 100

from array import *
import random


def find_missing_number(num_array: array) -> None:
    """Prints the missing number in an integer array of 1 to 100"""

    sum_1_to_100 = 100 * (100 + 1) / 2
    sum_array = sum(num_array)

    missing_number = sum_1_to_100 - sum_array

    print(int(missing_number))


def main() -> None:
    """Main function"""

    # creating an integer array
    integer_array = array("i", [])
    for i in range(1, 101):
        integer_array.append(i)

    # removing a random element from the array
    integer_array.pop(random.randint(1, 100))
    # print(integer_array.pop(random.randint(1, 100)))  # prints the removed number

    # finding the missing number
    find_missing_number(num_array=integer_array)


if __name__ == "__main__":
    main()
