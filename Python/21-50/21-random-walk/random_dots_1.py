# Draw random spots within the screen

import turtle as t
import random

# screen width and height
WIDTH = 800
HEIGHT = 600

# number of spots
REPETITION = 200

# speed of the turtle
SPEED = "fastest"

# size of dots
DOT_SIZE = 10


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
    turtly.penup()

    # change the turtle speed
    turtly.speed(SPEED)

    # draw the random walk
    for _ in range(REPETITION):

        # change the turtle color
        turtly.color(randomcolor())

        # random position within the screen
        (x, y) = random_position()

        # drawing the circle
        turtly.dot(DOT_SIZE)

        # making turtle move forward
        turtly.goto((x, y))

    # wait for user to close the window
    my_screen.exitonclick()


# calling the main function
if __name__ == "__main__":
    randomwalk()
