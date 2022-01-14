# write a program that calculates the sum of all the even numbers from 1 to 100. 
# Thus, the first even number would be 2 and the last one is 100.
# Output should just be the total sum.

# initializing sum of numbers to 0
sum = 0

# calculating the sum of all even numbers
for number in range(2, 101, 2):
        sum += number

''' Another method
for number in range(2, 101):
    if number % 2 == 0:
        sum += number
'''

# printing the sum of even numbers
print(sum)