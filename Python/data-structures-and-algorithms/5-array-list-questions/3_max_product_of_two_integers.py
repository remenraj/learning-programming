# Program to find maximum product of two integers in the array where all elements are positive

import numpy as np
import random


def max_product_of_two_integers(my_array: np.ndarray) -> int:
    """Finds the maximum product of two integers in the array"""

    # sort the array in ascending order
    sorted_array = np.sort(my_array)

    # print(sorted_array[-1], sorted_array[-2])
    # get the last two elements
    last_two_elements = sorted_array[-2:]

    print(last_two_elements)
    # get the product of the last two elements
    max_product = last_two_elements[0] * last_two_elements[1]

    # # another method
    # max product = 0
    # for i in range(len(my_array)):
    #     for j in range(i+1, len(my_array)):
    #         product = my_array[i] * my_array[j]
    #         if product > max_product:
    #             max_product = product
    #             pairs = [my_array[i], my_array[j]]
    #     print(pairs)

    return max_product


def main():
    """Main function"""
    # create an array of random integers
    my_array = np.array([])
    for i in range(10):
        my_array = np.append(my_array, random.randint(1, 30))
    print(my_array)

    print(
        f"Maximum product of two integers in the array is: {max_product_of_two_integers(my_array)}"
    )


if __name__ == "__main__":
    main()
