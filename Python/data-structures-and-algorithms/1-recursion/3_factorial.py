# program to find the factorial of a number using recursive method

# recursive method
def factorial(n):

    assert n >= 0 and int(n) == n, "Number must be positive integer"

    # base case
    if n in [0, 1]:
        return 1

    # recursive case
    else:
        return n * factorial(n - 1)


N = int(input("Enter a positive interger: "))
print(factorial(N))
