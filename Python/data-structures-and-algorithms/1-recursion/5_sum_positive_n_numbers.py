# Program to find the sum up to a positive integer number using recursion

# recursive method
def sum(n):

    # base case
    if n == 1:
        return 1
    # recursive case
    else:
        return n + sum(n - 1)


# main method
if __name__ == "__main__":
    try:
        # get the number from the user
        n = input(
            "Enter a positive integer number up to which sum is to be calculated: "
        )

        print(f"Sum up to {n} = {sum(int(n))}")

    # handle the exception
    except ValueError:
        # checking for the exception
        if type(n) == str:
            print("Enter a positive integer not a string")
        elif n < 1:
            print("Enter a positive integer")
