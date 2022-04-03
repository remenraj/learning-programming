# Find the greatest common divisor(GCD) of two numbers using recursion.

"""
Found using Euclidean Algorithm

gcd(48, 18)

Step 1: 48/18 = 2 remainder 12

Step 2: 18/12 = 1 remainder 6

Step 3: 12/6 = 2 remainder 0
    
gcd(a, 0) = a
gcd(a, b) = gcd(b, a % b)
"""


def gcd(a, b):

    assert int(a) == a and int(b) == b, "Number must be an integer"
    # checking for negative number
    if a < 0:
        a = -a
    # checking for negative number
    if b < 0:
        b = -b

    # base case
    if b == 0:
        return a

    # recursive case
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    print(gcd(18, -48))
