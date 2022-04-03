# Program to convert decimal to binary using recursion


# recursive method 1 to convert decimal to binary
def decimal_to_binary_1(n):

    assert int(n) == n, "Number must be an integer!"

    if n < 0:
        n = -n

    # base case
    if n == 0:
        return 1

    # recursive case
    else:
        quotient = n // 2
        remainder = n % 2
        decimal_to_binary_1(quotient)
        print(remainder, end="")


# recursive method 2 to convert decimal to binary
def decimal_to_binary_2(n):

    assert int(n) == n, "Number must be an integer"

    if n == 0:
        return 0

    else:
        return n % 2 + 10 * decimal_to_binary_2(n // 2)


if __name__ == "__main__":

    decimal_to_binary_1(-13)

    print(f"\n{decimal_to_binary_2(13)}")
