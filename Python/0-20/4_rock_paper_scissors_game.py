# Make a rock, paper, scissors game. 

import random

# storing ascii characters for rock, paper and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#creating the game list
game_list = [rock, paper, scissors]

#storing the user input.
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

#generating a random choice for the computer.
computer_choice = random.randint(0,2)

#checking for invalid entry and executing rest of the code if valid entry
if user_choice >= 0 and user_choice <= 2:
  print(game_list[user_choice])

  #printing computer's choice
  print(f"Computer chose:\n{game_list[computer_choice]}")

  #checking and printing the result of the game
  #checking for draw and printing the result
  if user_choice == computer_choice:
    print("It's a draw!")

  #checking for other conditions and printing the result
  elif user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif user_choice == 2 and computer_choice == 0:
    print("You lose!") 
  elif computer_choice > user_choice:
    print("You lose!")
  elif computer_choice < user_choice:
    print("You win!")

  '''old code
  elif user_choice == 0:
    if computer_choice == 1:
      print("You lost!")
    else:
      print("You win!")

  elif user_choice == 1:
    if computer_choice == 0:
      print("You win!")
    else:
      print("You lost!")

  elif user_choice == 2:
    if computer_choice == 0:
      print("You lost!")
    else:
      print("You win!")
  '''
#Checking for invalid entry
else:
  print("Invalid entry. You lost!")