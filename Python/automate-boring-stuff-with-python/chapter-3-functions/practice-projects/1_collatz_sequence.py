# Chapter 3: Functions, Page Number: 76
# Program to print the collatz sequence of a number


def collatz(number):
    # if number is even then divide it by 2
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    # if number is odd then multiply it by 3 and add 1
    else:
        print(3 * number + 1)
        return 3 * number + 1


# main function
def collatz_sequence():
    # get the number from user
    try:
        n = int(input("Enter a number:"))

    # if user enters a string then raise an exception
    except ValueError:
        print("Enter a valid positive number")
        return

    # calling the collatz function
    while n != 1:
        n = collatz(number=n)


# calling the main function
if __name__ == "__main__":
    collatz_sequence()
