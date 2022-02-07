####### Higher Lower Game #######
from art import logo, vs
from game_data import data
import random, os


def is_user_correct(follower_count1, follower_count2, choice_by_user):
    """Takes user guess, compare it with the follower count of two choices and return True if user guessed right"""
    # checking for the maximum value
    if follower_count1 > follower_count2:
        maxchoice = follower_count1
    else:
        maxchoice = follower_count2

    # checking if the user made the right choice
    if choice_by_user == maxchoice:
        return True
    else:
        return False


def compare(option1, option2, current_score):
    # clearing screen
    # for mac or linux platform
    if os.name == "posix":
        os.system("clear")

    # for windows platfrom
    else:
        os.system("cls")

    print(logo)

    # printing the current score
    if current_score > 0:
        print(f"You're right! Current score: {current_score}.")

    # printing 2 choices
    print(
        f"Compare A: {option1['name']}, {option1['description']}, {option1['country']}."
    )
    print(vs)
    print(
        f"Compare B: {option2['name']}, {option2['description']}, {option2['country']}."
    )

    valid_input = False
    while not valid_input:
        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_input == "a":
            user_choice = option1["follower_count"]
            valid_input = True
        elif user_input == "b":
            user_choice = option2["follower_count"]
            valid_input = True
        else:
            print("Invalid Input. Try again")
            valid_input = False

    # checking if the user is correct  and returning true if user got it correct
    return is_user_correct(
        follower_count1=option1["follower_count"],
        follower_count2=option2["follower_count"],
        choice_by_user=user_choice,
    )


def play_game():

    is_game_continue = True

    user_score = 0

    # cre
    options_are_same = True
    while options_are_same:
        first_option = random.choice(data)
        second_option = random.choice(data)

        if first_option != second_option:
            options_are_same = False

    while is_game_continue:

        is_game_continue = compare(
            option1=first_option, option2=second_option, current_score=user_score
        )

        if is_game_continue:

            first_option = second_option

            # creating a random second choice and checking if they are same
            options_are_same = True
            while options_are_same:
                second_option = random.choice(data)

                if first_option != second_option:
                    options_are_same = False

            user_score += 1

        else:
            # clearing screen
            # for mac or linux platform
            if os.name == "posix":
                os.system("clear")

            # for windows platfrom
            else:
                os.system("cls")

            print(logo)
            print(f"Sorry, that's wrong. Final score: {user_score}")
            is_game_continue = False


play_game()
