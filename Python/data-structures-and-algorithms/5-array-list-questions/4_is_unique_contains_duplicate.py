# Program to determine if a list has all unique characters, using python lists.

import random


def is_unique(my_list: list) -> bool:
    """Determines if the list has all unique characters"""

    new_list = []
    for i in range(len(my_list)):
        if my_list[i] in new_list:
            print(f"{my_list[i]} is not unique")
            return False
        else:
            new_list.append(my_list[i])

    # another method
    # # create a copy of the list
    # my_list_copy = my_list[:]

    # # check if the list has all unique characters
    # for i in range(len(my_list_copy)):
    #     if my_list_copy[i] in my_list[i+1:]:
    #         print(my_list_copy[i])
    #         return False

    return True


def main():
    """Main function"""
    my_list = []
    for i in range(20):
        my_list.append(random.randint(1, 100))

    print(my_list)
    # my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    print(f"Is the list unique? {is_unique(my_list)}")


if __name__ == "__main__":
    main()
