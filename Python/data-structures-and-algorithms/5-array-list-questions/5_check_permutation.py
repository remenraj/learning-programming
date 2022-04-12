# Given two lists, write a method to decide if one is a permutation of the other.


def permutation(list1: list, list2: list) -> bool:
    """Determines if the list has all unique characters"""

    # check if the length of the two lists are the same and return False if not
    if len(list1) != len(list2):
        return False
    #
    else:
        list1.sort()
        list2.sort()

        if list1 == list2:
            return True
        else:
            return False

        # # another method
        # for i in range(len(list1)):
        #     if list1[i] in list2:
        #         continue
        #     else:
        #         return False
        # return True


def main():
    # list_1 = [1, 2, 3, 4, 5]
    # list_2 = [2, 3, 1, 5, 4]

    list_1 = ["a", "b", "c", "d", "e"]
    list_2 = ["b", "c", "a", "e", "d"]

    print(permutation(list_1, list_2))


if __name__ == "__main__":
    main()
