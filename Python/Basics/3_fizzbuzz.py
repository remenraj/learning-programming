'''A program that automatically prints the solution to the FizzBuzz game.
Program should print each number from 1 to 100 in turn.
When the number is divisible by 3 then instead of printing the number it should print "Fizz".
When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
'''

# printing number from 1 to 100
for number in range(1, 101):
    
    # checking if the number is divisible by 3, 5 and printing Fizzbuzz if true
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    
    # checking if the number is divisible by 3 and printing Fizz if true
    elif number % 3 == 0:
        print("Fizz")
    
    # checking if the number is divisible by 5 and printing Buzz if true
    elif number % 5 == 0:
        print("Buzz")

    # printing the number which is divisible by 3 or 5
    else:
        print(number)
