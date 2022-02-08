# Program to draw hirst painting using turtle module

import turtle as t
import random
from data import color_list


def randomcolor():
    """Returns random tuple of r, g, b values from color_list"""

    return random.choice(color_list)


def painting():
    """Draws hirst painting using turtle module"""

    spot = t.Turtle()
    my_screen = t.Screen()

    # setting the color mode to max
    t.colormode(255)

    # changing the shape to turtle
    spot.hideturtle()

    # change the turtle speed
    spot.speed("fastest")

    # disabling pen draw
    spot.penup()

    # set initial postition
    x = -225
    y = -250
    spot.setpos(x, y)

    # moving up 10 times
    for yy in range(10):

        # drawing 10 spots horizontally
        for xx in range(10):

            spot.dot(20, randomcolor())

            """
            Another method to draw dots by drawing circles: 
            
            # set the fillcolor
            spot.fillcolor(randomcolor())

            # start the filling color
            spot.begin_fill()

            # drawing the circle of radius r
            spot.circle(10)

            # ending the filling of the color
            spot.end_fill()
            
            """
            spot.forward(50)

        # moving upwards
        y += 50
        spot.setpos(x, y)

    # closing the screen
    my_screen.exitonclick()


# calling the main function
if __name__ == "__main__":
    painting()
