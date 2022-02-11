from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        """Moves the paddle up"""
        self.sety(self.ycor() + 20)

    def down(self):
        """Moves the paddle down"""
        self.sety(self.ycor() - 20)
