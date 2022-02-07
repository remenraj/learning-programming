# Random walk program using turtle module
# Takes random directions from 0 to 360 degrees and goes to random position within the screen

import turtle as t
import random

# screen width and height
WIDTH = 800
HEIGHT = 600

# number of times turtle should move
REPETITION = 10000

# pen thickness
PEN_THICKNESS = 5

# speed of the turtle
SPEED = 3

# function to generate random color
def randomcolor():
    """Generates random color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


# function to goto random postion in the screen
def random_position():
    """Generates random position"""
    x = random.randint(-WIDTH / 2 + 10, WIDTH / 2 - 30)
    y = random.randint(-HEIGHT / 2 + 10, HEIGHT / 2 - 30)

    return (x, y)


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
    turtly.width(PEN_THICKNESS)

    # change the turtle speed
    turtly.speed(SPEED)

    # draw the random walk
    for _ in range(REPETITION):

        # change the turtle color
        turtly.color(randomcolor())

        # random position within the screen
        (x, y) = random_position()

        # change the turtle direction
        turtly.setheading(random.randint(0, 360))

        # making turtle move forward
        turtly.goto((x, y))

        # resetting turtle position when it goes out of screen
        if abs(turtly.xcor()) > (WIDTH / 2 - 30) or abs(turtly.ycor()) > (
            HEIGHT / 2 - 30
        ):
            (x, y) = random_position()
            turtly.goto((x, y))

    # wait for user to close the window
    my_screen.exitonclick()


# calling the main function
if __name__ == "__main__":
    randomwalk()
