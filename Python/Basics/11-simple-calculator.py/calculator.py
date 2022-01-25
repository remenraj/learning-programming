# simple calculator program
import os
from art import logo

# add
def add(n1, n2):
    return n1 + n2

# subtract
def subtract(n1, n2):
    return n1 - n2

# multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():

    print(logo)

    num1 = float(input("What's the first number?: "))

    is_continue = True

    while is_continue:

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))
        
        answer = operations[operation_symbol](n1=num1, n2=num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        

        correct_input = False
        while not correct_input:
            user_choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or type 'e' to exit: ")

            num1 = answer
            if user_choice == "y":
                num1 = answer
                correct_input = True
                is_continue = True

            elif user_choice == "n":
                correct_input = True
                is_continue = False

                # clearing the screen
                if os.name == 'posix': # for mac or linux platform
                    os.system('clear')
                else:
                    # for windows platfrom
                    os.system('cls')

                calculator()

            if user_choice == "e":
                correct_input = True
                is_continue = False

            else:
                correct_input = False
                is_continue = False
                print("Invalid Entry")

calculator()