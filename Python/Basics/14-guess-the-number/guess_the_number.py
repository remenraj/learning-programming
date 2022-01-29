import random, os
from tkinter import E
from art import logo, high, low, winner, guess_over

EASY_LEVEL = 10
HARD_LEVEL = 5

# welcome message
def welcome_message():
    # guess the number logo
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

# user choice for difficulty level
def difficulty_level():

    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        return EASY_LEVEL

    elif level == "hard":
        return HARD_LEVEL

    else:
        return 0

# random number generator
def random_number_generator():
    """returns a random number between 0 and 100"""
    return random.randint(0, 100)

# checking the guessed number with correct number
def check_guess(correct_number, attempts_remaining):

    print(f"You have {attempts_remaining} attempts to guess the number.")
    user_guess = int(input("Make a guess: "))

    if user_guess == correct_number:
        return True
    elif user_guess < correct_number:
        print(low)
        return False
    elif user_guess > correct_number:
        print(high)
        return False

# game function
def play_game():

    welcome_message()

    total_attempts = difficulty_level()
    while total_attempts == 0:
        print("Invalid Entry. Try again")
        total_attempts = difficulty_level()

    is_game_over = False
    number = random_number_generator()

    while not is_game_over:
        is_game_over = check_guess(correct_number=number, attempts_remaining=total_attempts)
        total_attempts -= 1

        if total_attempts == 0:
            print(guess_over)
            is_game_over = True

        elif is_game_over == True:
            print(f"{winner}\nThe answer was {number}.")


play_game()

# continue or not
should_continue = True

while should_continue:

    is_continue = input("\nDo you want to play the number guessing game again? Type \'y\' or \'n\': ")

    if is_continue == "y":
        if os.name == 'posix': # for mac or linux platform
            os.system('clear')
        else:
            # for windows platfrom
            os.system('cls')
        play_game()   
        
    elif is_continue == "n":
        should_continue = False

    else:
        print("Invalid Entry. Try again")