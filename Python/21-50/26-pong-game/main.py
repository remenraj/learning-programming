# pong game
import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from screensettings import WIDTH, HEIGHT
from scoreboard import ScoreBoard


def pong_game():
    # set up the screen
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.title("Pong Game")
    screen.tracer(0)
    screen.listen()

    # set up paddle and ball
    left_paddle = Paddle((-350, 0))
    right_paddle = Paddle((350, 0))
    ball = Ball()

    # initializing scoreboard
    score = ScoreBoard()

    # listening for key presses
    screen.onkeypress(fun=left_paddle.up, key="w")
    screen.onkeypress(fun=left_paddle.down, key="s")
    screen.onkeypress(fun=right_paddle.up, key="Up")
    screen.onkeypress(fun=right_paddle.down, key="Down")

    game_is_on = True
    while game_is_on:
        # refresh screen
        screen.update()
        time.sleep(ball.moving_speed)

        # making the ball move
        ball.move()

        # making the ball bounce with the wall
        if abs(ball.ycor()) > HEIGHT / 2 - 30:
            ball.wall_bounce()

        # making the ball bounce with the paddle
        if (ball.distance(right_paddle) < 50 and abs(ball.xcor()) > WIDTH / 2 - 75) or (
            ball.distance(left_paddle) < 50 and abs(ball.xcor()) > WIDTH / 2 - 75
        ):
            ball.paddle_bounce()
            ball.increase_ball_speed()

        # checking if the right paddle misses the ball
        if ball.xcor() > WIDTH / 2:
            ball.reset_and_switch_direction()
            score.update_left_score()

        # checking if the left paddle misses the ball
        if ball.xcor() < -(WIDTH / 2):
            ball.reset_and_switch_direction()
            score.update_right_score()

    # closing the screen on mouseclick
    screen.exitonclick()


if __name__ == "__main__":
    pong_game()
