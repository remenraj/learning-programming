# prime number checker

# function for checking whether a number is prime or not
def prime_checker(number):

    is_prime = True

    if number <= 1:
        is_prime = False

    else:     
        for num in range(2, number):
            if number % num == 0:
                is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
            
  
# prompting user for a number
number_to_be_checked = int(input("Check this number: "))

#calling the function and passing the number as argument
prime_checker(number=number_to_be_checked)