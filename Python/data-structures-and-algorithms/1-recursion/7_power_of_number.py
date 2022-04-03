# Program to find the power of a number using recursion


def power_of_number(base, power):

    assert power >= 0 and int(power) == power, "Power has to be a positive integer!"

    # base case
    if power == 1:
        return base
    elif power == 0:
        return 1

    # recursive case
    else:
        return base * power_of_number(base, power - 1)


# main method
if __name__ == "__main__":

    print(power_of_number(base=3.2, power=3))
