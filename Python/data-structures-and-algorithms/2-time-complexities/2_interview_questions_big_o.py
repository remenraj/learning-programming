################ Interview Questions #############
# Question1
# O(n)
def foo(array):
    sum = 0  # O(1)
    product = 1  # O(1)
    for i in array:  # O(n)
        sum += i  # O(1)
    for i in array:  # O(n)
        product *= i  # O(1)
    print("Sum = " + str(sum) + ", Product = " + str(product))  # O(1)


ar1 = [1, 2, 3, 4]
foo(ar1)  # O(n)

# Question2

# O(n^2)
def printPairs(array):
    for i in array:  # O(n^2)
        for j in array:  # O(n)
            print(str(i) + "," + str(j))  # O(1)


# Question3
# O(n^2)
def printUnorderedPairs(array):
    for i in range(0, len(array)):  # O(n^2)
        for j in range(i + 1, len(array)):  # O(n/2)=O(n)
            print(array[i] + "," + array[j])  # O(1)


# Question4
# Time complexity = O(len(arrayB) * len(arrayA))
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):  # O(len(arrayA))
        for j in range(len(arrayB)):  # O(len(arrayB))
            if arrayA[i] < arrayB[j]:  # O(1)
                print(str(arrayA[i]) + "," + str(arrayB[j]))  # O(1)


arrayA = [1, 2, 3, 4, 5]
arrayB = [2, 6, 7, 8]


# Question5
# Time complexity = O(len(arrayB) * len(arrayA))
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):  # O(len(arrayB) * len(arrayA))
        for j in range(len(arrayB)):  # O(len(arrayB))
            for k in range(0, 100000):  # O(1)
                print(str(arrayA[i]) + "," + str(arrayB[j]))  # O(1)


# printUnorderedPairss(arrayA,arrayB)


# Question6
# Time complexity = O(N)
def reverse(array):
    for i in range(0, int(len(array) / 2)):  # O(len(array)/2)= O(N)
        other = len(array) - i - 1  # O(1)
        temp = array[i]  # O(1)
        array[i] = array[other]  # O(1)
        array[other] = temp  # O(1)
    print(array)  # O(1)


reverse(arrayA)


# Question7
# Which of the following are equivalent to O(N)? Why?

# O(N + P), where P < N/2   ==  O(N), P is less than N and is dropped
# O(2N) ==  O(N), constants are dropped
# O(N + logN)   ==  O(N), logN is less than N from Big-O complexity chart
# O(N + NlogN)  ==  NlogN, here NlogN is dominant, N is dropped
# O(N + M)  ==  O(N + M), there's no established relation between N and M. And they both are variables.

# Question8

# Time complexity = O(N)
def factorial(n):  # M(n)
    if n < 0:  # O(1)
        return -1  # O(1)
    elif n == 0:  # O(1)
        return 1  # O(1)
    else:
        return n * factorial(n - 1)  # M(n-1)


# M(n) = O(1) + M(n-1)
# M(0) = O(1)
# M(n-1) = O(1) + M((n-1) -1)
# M(n-2) = O(1) + M((n-2) -1)

# M(n) = O(1) + M(n-1)
#      = 1 + M(n-1)
#      = 1 + O(1) + M((n-1) -1) = 2 + M(n-2)
#      = 3 + M(n-3)
#      = a + M(n-a) = n + M(n-n)
#      = n + 1 = n

print(factorial(3))

# Question9
# O(2^N)

def allFib(n):
    for i in range(n):  # O(N)
        print(str(i) + ":, " + str(fib(i))) # M(n)


def fib(n):
    if n <= 0:  # O(1)
        return 0    # O(1)
    elif n == 1:    # O(1)
        return 1    # O(1)
    return fib(n - 1) + fib(n - 2)  # O(2^N)


allFib(4)

# Question10
# O(logN)
def powersOf2(n):
    # print("n:"+str(n))
    if n < 1:   # O(1)
        return 0    # O(1)
    elif n == 1:    # O(1)
        print(1)    # O(1)
        return 1    # O(1)
    else:
        prev = powersOf2(int(n / 2))    # O(logN)
        # print("prev:"+str(prev))
        print(prev) # O(1)
        curr = prev * 2 # O(1)
        print(curr) # O(1)
        return curr


powersOf2(50)
