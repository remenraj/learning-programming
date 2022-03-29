# program to display fibonacci number series

# recursive method
def fibonacci(n):

    assert n >= 0 and int(n) == n, "Number must be a positive integer."

    # base case
    if n in [0, 1]:
        return n

    # recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# ask user for input
N = int(input("Enter a positive integer: "))

# looping through fibonacci series
for i in range(0, N + 1):

    # printing fibonacci series
    print(fibonacci(i), end=" ")
