#!/usr/bin/env python3

### TURTLE CROSSING GAME ###

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from screen_settings import HEIGHT, WIDTH
import random


def turtle_crossing():
    # Create the screen
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.tracer(0)
    screen.listen()

    # Create the player
    player = Player()

    # Detect keyboard input
    screen.onkeypress(fun=player.move_up, key="Up")

    # Create the car manager
    car = CarManager()

    # Create the scoreboard
    score = Scoreboard()

    game_is_on = True
    while game_is_on:
        # Update the screen
        time.sleep(0.1)
        screen.update()

        # Create and move the cars
        car.generate_cars()
        car.move_cars()

        # Detect if the player has collided with a car and end the game
        for i in range(len(car.cars)):
            if player.distance(car.cars[i]) < 30:
                game_is_on = False

        # Detect if the player has reached the finish line and increase the score, speed of cars
        if player.detect_top():
            score.update_scoreboard()
            car.increase_speed()

    # display the game over screen
    score.game_over()

    # Close the screen
    screen.exitonclick()


# Start the game
if __name__ == "__main__":
    turtle_crossing()
