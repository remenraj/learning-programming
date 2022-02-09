#### Turtle Race Game ####
# User can bet on which color turtle will win the race

import turtle as t
import random


# main function
def turtle_race():
    # setting up screen
    screen = t.Screen()
    screen.setup(width=500, height=400)

    user_bet = screen.textinput(
        title="Make your bet",
        prompt="Which turtle will win the race? Enter a color in rainbow: ",
    )

    color_list = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

    # creating an empty list of turtles
    runners = []
    # initial turtle count
    turtle_count = 0
    # y position of first turtle
    y_axis = -130

    # creating total turtles with different color from color_list
    for color in color_list:

        # creating the turtle
        runners.append(t.Turtle(shape="turtle"))

        # changing the color to one from the color_list
        runners[turtle_count].color(color_list[turtle_count])

        # disable drawing
        runners[turtle_count].penup()

        # making the turtle go to the start position
        runners[turtle_count].goto(x=-230, y=y_axis)

        y_axis += 40
        turtle_count += 1

    is_race_on = False

    if user_bet:
        is_race_on = True

    # racing till any of the turtle reaches the end of screen
    while is_race_on:

        # loop for making turtles move randomly
        for runner in runners:

            if runner.xcor() > 220:
                # race over
                is_race_on = False

                # winning color of turtle
                winning_color = runner.pencolor()

                # checking if the user bet is correct
                # and printing the result on the terminal
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")

                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")

            # making the turtle move
            runner.forward(random.randint(0, 10))

    # closing the window
    screen.exitonclick()


# calling the main function
if __name__ == "__main__":
    turtle_race()
