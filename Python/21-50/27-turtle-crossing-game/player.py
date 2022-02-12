from turtle import Turtle
from screen_settings import HEIGHT, WIDTH


STARTING_POSITION = (0, -(HEIGHT / 2 - 20))
MOVE_DISTANCE = 10
FINISH_LINE_Y = HEIGHT / 2 - 20


# Player class
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("darkgreen")
        self.shape("turtle")
        self.setheading(90)
        self.setposition(STARTING_POSITION)

    def move_up(self):
        """Move the player up"""
        self.forward(MOVE_DISTANCE)

    def detect_top(self):
        """Detect if the player has reached the finish line and return True if so"""
        if self.ycor() > HEIGHT / 2 - 60:
            self.setposition(STARTING_POSITION)
            return True
        else:
            return False
