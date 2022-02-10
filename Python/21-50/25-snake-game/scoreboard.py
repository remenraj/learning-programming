from turtle import Turtle
from screen import WIDTH, HEIGHT

# scoreboard settings
# position of scoreboard
SCORE_X = 0
SCORE_Y = HEIGHT / 2 - 30

# scoreboard alignment and font
SCORE_ALIGNMENT = "center"
SCORE_FONT = ("courier", 12, "normal")

# game over message settings
GAME_OVER_FONT = ("courier", 24, "normal")
GAME_OVER_ALIGNMENT = "center"

# data directory
DIRECTORY = r"learning-programming\Python\21-50\25-snake-game\data.txt"


class Score(Turtle):
    def __init__(self):

        super().__init__()

        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(SCORE_X, SCORE_Y)

        with open(DIRECTORY) as data:
            self.highscore = int(data.read())

        self.display_score()

    def display_score(self):
        """Displays score on the screen"""
        self.write(
            f"Score: {self.score}    High Score: {self.highscore}",
            align=SCORE_ALIGNMENT,
            font=SCORE_FONT,
        )

    def refresh(self):
        """Refreshes the score on the screen"""
        self.clear()
        self.display_score()

    def reset(self):
        """Resets the score and updates high score data"""
        if self.score > self.highscore:
            with open(
                DIRECTORY,
                mode="w",
            ) as data:
                data.write(str(self.score))
            self.highscore = self.score
        self.score = 0
        self.refresh()

    def update_score(self):
        """Updates the score"""
        self.score += 1
        self.refresh()
