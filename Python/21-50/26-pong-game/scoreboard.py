from turtle import Turtle
from screensettings import HEIGHT, WIDTH


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard"""
        self.clear()
        # left player score
        self.goto(-WIDTH / 4, HEIGHT / 2 - 100)
        self.write(self.left_score, align="center", font=("Courier", 50, "normal"))
        # right player score
        self.goto(WIDTH / 4, HEIGHT / 2 - 100)
        self.write(self.right_score, align="center", font=("Courier", 50, "normal"))

    def update_left_score(self):
        """Updates the left score"""
        self.left_score += 1
        self.update_scoreboard()

    def update_right_score(self):
        """Updates the right score"""
        self.right_score += 1
        self.update_scoreboard()
