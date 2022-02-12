from turtle import Turtle
from screen_settings import HEIGHT


FONT = ("Courier", 24, "normal")

# Scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.score = 1
        self.goto(x=0, y=HEIGHT / 2 - 40)
        self.write(f"Level : {self.score}", align="center", font=FONT)

    def update_scoreboard(self):
        """Update the scoreboard"""
        self.clear()
        self.score += 1
        self.goto(x=0, y=HEIGHT / 2 - 40)
        self.write(f"Level : {self.score}", align="center", font=FONT)

    def game_over(self):
        """Display the game over screen"""
        self.clear()
        self.goto(x=0, y=HEIGHT / 2 - 40)
        self.write(f"Level : {self.score}", align="center", font=FONT)

        self.goto(x=0, y=0)
        self.write("Game Over", align="center", font=FONT)
