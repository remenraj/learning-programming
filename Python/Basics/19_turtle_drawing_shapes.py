# turtle program that draws a triangle up to decagon
# And changes its color after drawing a shape using turtle module

from turtle import Turtle, Screen
import random

# function to return a random color
def changecolor():

    R = random.randrange(0, 255, 10)
    G = random.randrange(0, 255, 10)
    B = random.randrange(0, 255, 10)

    return R, G, B


def drawshapes():
    #
    turtly = Turtle()
    my_screen = Screen()

    # changing the shape to turtle
    turtly.shape("turtle")

    # setting the colormode of screen
    my_screen.colormode(255)

    # change the turtle speed
    turtly.speed(1)

    # initialize sides
    sides = 3

    # loop to draw shapes
    for i in range(8):

        # changing the color of turtle
        turtly.color(changecolor())

        # drawing shapes
        for j in range(sides):
            turtly.forward(50)
            turtly.right(360 / sides)

        # increasing the number of sides of the shape by one
        sides += 1

    # not closing the screen till mouse click
    my_screen.exitonclick()


if __name__ == "__main__":
    drawshapes()
