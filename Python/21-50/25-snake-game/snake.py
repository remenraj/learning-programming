from turtle import Turtle
from screen import HEIGHT, WIDTH

# snake settings
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
MOVING_SPEED = 10

# directions for key binding
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):

        # empty list to contain snake body
        self.snake_body = []
        self.create_snake_body()
        self.head = self.snake_body[0]

    def create_snake_body(self):
        """Creates starting snake body"""
        new_body_part = Turtle(shape="square")
        new_body_part.penup()
        new_body_part.color("white")
        self.snake_body.append(new_body_part)
        self.head = self.snake_body[0]

        # creating initial snake body parts
        for position in STARTING_POSITION[1:]:
            self.extend()

    def extend(self):
        """Adds a new body part to the snake"""

        position = self.snake_body[-1].position()

        new_body_part = Turtle(shape="square")
        new_body_part.penup()
        new_body_part.color("white")
        new_body_part.goto(position)
        self.snake_body.append(new_body_part)

    def reset(self):
        """Resets the snake"""
        for body_part in self.snake_body:
            body_part.goto(2 * WIDTH, 2 * HEIGHT)

        self.snake_body.clear()
        self.create_snake_body()
        self.head = self.snake_body[0]

    def move(self):
        """Makes the snake move forward"""
        for body_num in range(len(self.snake_body) - 1, 0, -1):

            new_x = self.snake_body[body_num - 1].xcor()
            new_y = self.snake_body[body_num - 1].ycor()

            self.snake_body[body_num].goto(new_x, new_y)

        self.head.forward(MOVING_DISTANCE)

    # functions for key binding
    def up(self):
        """Turn north"""
        # not allowing snake to go up if facing down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turn south"""
        # not allowing snake to go down if facing up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turn left"""
        # not allowing snake to go left if facing right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turn right"""
        # not allowing snake to go right if facing left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
