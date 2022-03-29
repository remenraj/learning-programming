# Program to find the sum of digits of a positive integer number using recursion

# recursive method to find the sum of digits of a positive integer number
def sum_digits(n):

    assert int(n) == n, "The number has to be an integer!"

    # base case
    remainder = n % 10
    quotient = n // 10
    if quotient == 0:
        return remainder

    # recursive case
    else:
        return remainder + sum_digits(quotient)


# main method
if __name__ == "__main__":
    try:

        print("Find the sum of digits of a positive integer number using recursion")
        n = int(input("Enter a number : "))
        print(f"Sum of digits of the number is : {sum_digits(abs(n))}")

    # handle the exception
    except ValueError:
        print("Enter a valid integer number")
        exit()
