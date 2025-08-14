from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 275)
        self.write(f"{self.score_l} | {self.score_r}", align="center", font=("Courier", 15, "normal"))

    def increase_score_l(self):
        self.score_l += 1
        self.update_scoreboard()
    def increase_score_r(self):
        self.score_r += 1
        self.update_scoreboard()