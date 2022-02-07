# Random walk program using turtle module
# Takes random turns at 90 degrees and moves forward
# Resets to (0, 0) when it goes out of screen

import turtle as t
import random

# screen width and height
WIDTH = 800
HEIGHT = 600

# number of times turtle should move
REPETITION = 10000

# function to generate random color
def randomcolor():
    """Generates random color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


# main function
def randomwalk():

    # setting up screen
    t.colormode(255)
    my_screen = t.Screen()
    my_screen.setup(width=WIDTH, height=HEIGHT)

    # creating turtle
    turtly = t.Turtle()

    # hiding turtle
    turtly.hideturtle()

    # change turtle width
    turtly.width(15)

    # change the turtle speed
    turtly.speed("fastest")

    # draw the random walk
    for _ in range(REPETITION):

        # change the turtle color
        turtly.color(randomcolor())

        # making turtle move forward
        turtly.forward(30)

        # making random turn
        coin_toss = random.randint(1, 2)
        if coin_toss % 2 == 0:
            turtly.right(90)
        else:
            turtly.left(90)

        # resetting turtle position when it goes out of screen
        if abs(turtly.xcor()) > (WIDTH / 2 - 30) or abs(turtly.ycor()) > (
            HEIGHT / 2 - 30
        ):
            turtly.penup()
            turtly.goto(0, 0)
            turtly.pendown()

    # wait for user to close the window
    my_screen.exitonclick()


# calling the main function
if __name__ == "__main__":
    randomwalk()
