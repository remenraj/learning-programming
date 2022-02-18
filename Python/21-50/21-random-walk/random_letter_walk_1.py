# Program to write random letters on the screen using turtle module

import turtle as t
import random


def random_letter():
    """Returns a random letter"""
    letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
    return random.choice(letters)

def painting():
    """Draws random letters on the screen"""

    spot = t.Turtle()
    my_screen = t.Screen()
    my_screen.setup(width=700, height=700)

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
    for yy in range(12):

        # drawing 10 spots horizontally
        for xx in range(12):
            spot.write(random_letter(), align="center", font=(20))
            spot.forward(50)

        # moving upwards
        y += 50
        spot.setpos(x, y)

    # closing the screen
    my_screen.mainloop()


# calling the main function
if __name__ == "__main__":
    painting()
