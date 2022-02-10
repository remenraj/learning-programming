########### SNAKE GAME ###########
# This is a snake game using Turtle module

import time
from turtle import Turtle, Screen, width
from snake import Snake
from food import Food
from screen import HEIGHT, WIDTH
from scoreboard import Score


# setting up screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# creating snake
snake = Snake()

# creating food
food = Food()

# creating scoreboard
score = Score()

# listening for key presses
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_on = True
while game_is_on:
    # updating the screen
    screen.update()
    time.sleep(0.1)

    # making snake move
    snake.move()

    # detecting collision with food
    if snake.head.distance(food) < 15:
        # generating new food
        food.refresh()
        snake.extend()

        # updating score
        score.update_score()

    # detecting collision with wall
    if abs(snake.head.xcor()) > (WIDTH / 2 - 10) or abs(snake.head.ycor()) > (
        HEIGHT / 2 - 10
    ):
        score.reset()
        snake.reset()

    # detecting collision with itself
    for body_part in snake.snake_body[1:]:
        if snake.head.distance(body_part) < 5:
            score.reset()


# closing screen
screen.exitonclick()
