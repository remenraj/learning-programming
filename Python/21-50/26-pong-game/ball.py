from turtle import Turtle
from screensettings import HEIGHT, WIDTH
from random import randint, choice

MOVING_DISTANCE = 10

# heading_list = [randint(135, 180), randint(181, 225), randint(0, 45), randint(315, 360)]
# BALL_HEADING_ANGLE = randint(0, 360)
# BALL_HEADING_ANGLE = choice(heading_list)


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.setposition(x=0, y=0)
        self.moving_speed = 0.1
        # self.setheading(BALL_HEADING_ANGLE)

        self.add_x = MOVING_DISTANCE
        self.add_y = MOVING_DISTANCE

    def move(self):
        """Moves the ball"""
        # make ball move forward
        # self.forward(MOVING_DISTANCE)
        new_x = self.xcor() + self.add_x
        new_y = self.ycor() + self.add_y

        self.goto(new_x, new_y)

    def wall_bounce(self):
        """Makes the ball bounce with the wall"""
        # self.setheading(360 - self.heading())
        # self.forward(MOVING_DISTANCE)
        self.add_y = -self.add_y

    def paddle_bounce(self):
        """Makes the ball bounce with the paddle"""
        self.add_x = -self.add_x

        # if self.heading() < 90 or self.heading() > 270:
        #     self.setheading(180 - self.heading())
        #     self.forward(MOVING_DISTANCE)

        # else:
        #     self.setheading(90 + self.heading())
        #     self.forward(MOVING_DISTANCE)

    def reset_and_switch_direction(self):
        """Resets the ball, switch the direction and speed"""

        self.setposition(0, 0)
        self.moving_speed = 0.1
        self.add_x = -self.add_x

    def increase_ball_speed(self):
        """Increases the ball speed"""
        self.moving_speed *= 0.5
