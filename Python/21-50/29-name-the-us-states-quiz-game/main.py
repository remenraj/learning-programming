#! /usr/bin/env python3

# US states quiz game

import turtle, pandas

# file directories
IMAGE_DIR = r"learning-programming\Python\21-50\29-name-the-us-states-quiz-game\blank_states_img.gif"
STATE_CSV_FILE_DIR = (
    r"learning-programming\Python\21-50\29-name-the-us-states-quiz-game\50_states.csv"
)
MISSED_STATE_CSV_FILE_DIR = (
    r"learning-programming\Python\21-50\29-name-the-us-states-quiz-game"
)

# font of text on screen
FONT = ("Courier", 10, "normal")

# setting up screen
screen = turtle.Screen()
screen.setup(width=730, height=495)
screen.title("US States Quiz")
image = IMAGE_DIR
screen.addshape(image)
turtle.shape(image)

# # code to print the location of mouse click
# def get_state_name(x, y):
#     print(x, y)
# turtle.onscreenclick(get_state_name)

score = 0
correct_ans_list = []

# creating states dataframe
df = pandas.read_csv(STATE_CSV_FILE_DIR)

# creating the list of all 50 US states from the dataframe
state_list = df.state.to_list()


# game is on till user guessed all US states or the user entered 'Exit' in the textbox
is_game_on = True
while is_game_on and len(correct_ans_list) < 50:
    user_answer = screen.textinput(
        title=f"{score}/50 States Correct", prompt="Enter the state name"
    ).title()

    # exiting the game early
    if user_answer == "Exit":
        # creating a dictionary of missed states
        missed_states = {}
        missed_states["Missed States"] = [
            state for state in state_list if state not in correct_ans_list
        ]

        # converting missed states dictionary into dataframe
        new_data = pandas.DataFrame(data=missed_states)

        # saving dataframe into csv file
        new_data.to_csv(f"{MISSED_STATE_CSV_FILE_DIR}\\missed_states.csv")
        break
    
    # displaying guessed state in the map
    if user_answer in state_list:
        score += 1
        correct_ans_list.append(user_answer)
        index = state_list.index(user_answer)
        new_state_data = df[df.state == user_answer]

        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.speed(3)
        new_state.goto(x=int(new_state_data.x), y=int(new_state_data.y))
        new_state.write(f"{new_state_data.state.item()}", align="center", font=FONT)


# turtle.mainloop()
