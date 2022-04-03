# Program to find the biggest number in an array
from random import randint


def largest_number(numbers, n):
    """Recursive function to find the biggest number in a list"""
    if n == 1:
        return numbers[0]

    return max(numbers[n - 1], largest_number(numbers, n - 1))


if __name__ == "__main__":

    # creating an array of random numbers
    numbers = []
    for _ in range(20):
        numbers.append(randint(1, 100))

    print(f"List: {numbers}")

    # finding the biggest number in the array
    number = len(numbers)
    big_number = largest_number(numbers, number)

    print(f"The biggest number is {big_number}")
