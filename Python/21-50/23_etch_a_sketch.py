# A simple Etch-A-Sketch program using turtle module

import turtle as t


def forward():
    """Move forwards"""
    sketch.forward(10)


def backward():
    """Move backwards"""
    sketch.backward(10)


def clockwise():
    """Turn to right"""
    sketch.right(10)


def counterclockwise():
    """Turn to left"""
    sketch.left(10)


def clear():
    """Clear screen and reset turtle postion"""
    sketch.reset()


# setting up turtle and screen
sketch = t.Turtle()
screen = t.Screen()

# initiating screen to listen to keypress
screen.listen()

# binding keypress to various activities
screen.onkeypress(key="w", fun=forward)
screen.onkeypress(key="s", fun=backward)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="a", fun=counterclockwise)

# clearing the screen and reseting the position of turtle
screen.onkeypress(key="c", fun=clear)

# closing the screen
screen.exitonclick()
