# secret auction program
import os
os.system('cls')  # on windows
# os.system('clear')  # on linux / os x

from art import logo
print(logo)
print("Welcome to the secret auction program")


is_continue = True

# creating an empty dictionary to store the name and corresponding bid.
secret_auction = {}

while is_continue:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))

    secret_auction[name] = bid

    # checking for other bidders
    continue_or_not = input("Are there any other bidders? Type 'y' or 'n': ")

    if continue_or_not == "n":
        is_continue = False

    # clearing the screen
    if os.name == 'posix': # for mac or linux platform
      os.system('clear')
    else:
      # for windows platfrom
      os.system('cls')

# finding the winner of the secret auction
winner = max(secret_auction, key= secret_auction.get)

# showing the winner of the secret auction
print(f"Winner is {winner} with a bid of ${secret_auction[winner]}.")