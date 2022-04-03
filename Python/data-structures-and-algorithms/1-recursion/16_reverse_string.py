# Program to reverse a string using recursion

# recursive function
def reverse(strng):
    # base case
    if len(strng) <= 1:
        return strng

    # recursive case
    return strng[-1] + reverse(strng[:-1])


# calling the main function
if __name__ == "__main__":
    print(reverse("python"))  # 'nohtyp'
    print(reverse("appmillers"))  # 'srellimppa'
