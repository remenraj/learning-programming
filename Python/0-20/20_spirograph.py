# drawing spirograph using turtle module
import turtle as t
import random

# function to return random color
def randomcolor():
    """Returns a random tuple of red, green, blue color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


def spirograph():

    # setting the color mode to max
    t.colormode(255)

    turtly = t.Turtle()
    my_screen = t.Screen()

    # changing the shape to turtle
    turtly.hideturtle()

    # change the turtle speed
    turtly.speed("fastest")

    # radius of circle
    radius = 100

    # initial tilt = 0
    tilt = 0

    # number of circles in the spirograph
    gap_between_circles = 5

    # loop for printing spirograph
    for i in range(int(360 / gap_between_circles)):

        # changing the color of the turtle
        turtly.color(randomcolor())

        # drawing the circle
        turtly.circle(radius)

        # increasing the tilt of the circle
        tilt += gap_between_circles

        turtly.setheading(tilt)

    """ 
    ###### ANOTHER METHOD TO DRAW SPIROGRAPH ######
    
    # number of circles in the spirograph
    total_circles = 55

    # loop for printing spirograph
    for i in range(total_circles):

        # changing the color of the turtle
        turtly.color(randomcolor())

        # drawing the circle
        turtly.circle(radius)

        # increasing the tilt of the circle
        tilt += 360 / total_circles
        turtly.setheading(tilt)"""

    # showing the screen until mouse click
    my_screen.exitonclick()


spirograph()
