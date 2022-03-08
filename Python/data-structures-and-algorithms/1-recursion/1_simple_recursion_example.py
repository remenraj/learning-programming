# simple recursion
def recursiveMethod(n):

    if n < 1:
        print("n is less than 1")
    else:
        recursiveMethod(n - 1)

        print(n)


recursiveMethod(5)


# stack memory is used by the system for managing recursive calls.
# stack memory manages the value based on last in first out.
