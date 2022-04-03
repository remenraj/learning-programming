# Program to check if a string is palindrome or not

# recursive function to check if a string is palindrome or not
def isPalindrome(strng):

    # base case
    if len(strng) == 0:
        return True
    if strng[0] != strng[-1]:
        return False

    # recursive case
    return isPalindrome(strng[1:-1])


if __name__ == "__main__":
    print(isPalindrome("awesome"))  # false
    print(isPalindrome("foobar"))  # false
    print(isPalindrome("tacocat"))  # true
    print(isPalindrome("amanaplanacanalpanama"))  # true
    print(isPalindrome("amanaplanacanalpandemonium"))  # false
