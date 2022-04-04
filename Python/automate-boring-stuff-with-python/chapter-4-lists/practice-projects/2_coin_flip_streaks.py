# chapter 4: Lists
# Practice Project: Coin Flip Streaks, page number: 107

# program to find out how often a streak of six heads or a streak
# of six tails comes up in a randomly generated list of heads and tails.

import random


coin_flip = ["H", "T"]

number_of_streaks = 0

# loop that repeats the experiment 10,000 times so we can find out what percentage of the 
# coin flips contains a streak of six heads or tails in a row.
for experiment_number in range(10000):
    
    # Code that creates a list of 100 'heads' or 'tails' values.
    flipped_result = []
    for _ in range(100):
        flipped_result.append(random.choice(coin_flip))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(flipped_result) - 5):
        # # method 1:
        # if flipped_result[i] == flipped_result[i + 1] == flipped_result[i + 2] == flipped_result[i + 3] == flipped_result[i + 4] == flipped_result[i + 5]:
        #     number_of_streaks += 1

        # method 2:
        temp_list = flipped_result[i:i + 6]
        is_streak = temp_list.count(temp_list[0]) == 6
        if is_streak:
            number_of_streaks += 1
        
print(f'Chance of streak: {number_of_streaks / 100}%')
