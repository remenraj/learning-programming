############### Blackjack Game #####################

import art, random, os

# function that returns random cards
def deal_card():
    '''Returns a random card from the deck.'''
    # list of scores of all cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# function that calculates and returns the total score
def calculate_score(score_list):
    """Calculates and returns the total score"""

    # checking for blackjack
    if len(score_list) == 2 and 11 in score_list and 10 in score_list:
        return 0

    # checking for ace and returning the total score
    elif 11 in score_list:

        total_score = sum(score_list)
        
        if total_score > 21:
            for index in range(0, len(score_list)):
                if score_list[index] == 11:
                    score_list[index] = 1

        return sum(score_list)

    return sum(score_list)

def compare(user_score, computer_score):

  # if user and the computer are both over, user loses.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if user_score == computer_score:
    return "Draw 🤗"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"


def play_game():
    # printing logo
    print(art.logo)

    # initializing empty list for user and dealer
    user_cards = []
    computer_cards = []
    is_game_over = False
    # getting 2 random cards for user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        # calculating the score of user and computer
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # printing user's cards and total score
        print(f"\nYour cards: {user_cards}, current score: {user_score}")

        # printing computer's first hand
        print(f"\nComputer's first hand: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # promting user to get another card or pass
            hit_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")

            if  hit_or_pass == "y":
                # taking another card
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # printing final hand of user
    print(f"\nYour final hand: {user_cards}, Final score: {user_score}")

    # printing final hand of computer
    print(f"\nComputer's final hand: {computer_cards}, Final score: {computer_score}")
    
    print(compare(user_score, computer_score))

should_continue = True


while should_continue:

    is_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

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
        print("Invalid Entry")
