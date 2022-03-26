# program to find power of two

# power of 2
N = 3

# recursive method
def power_of_two_recursion(n):

    # base case
    if n == 0:
        return 1

    # recursive case
    else:
        return 2 * power_of_two_recursion(n - 1)


# iterative method
def power_of_two_iteration(n):

    # base case
    product = 1

    # loop to find 2^n
    for _ in range(n):
        product *= 2

    return product


print(power_of_two_recursion(N))
print(power_of_two_iteration(N))
