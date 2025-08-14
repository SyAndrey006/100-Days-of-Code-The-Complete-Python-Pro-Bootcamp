from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score()


    def update_score(self):
        self.clear()
        self.position()
        self.write(f"Level: {self.level}", font=FONT, align="left")


    def position(self):
        self.goto(-280, 260)

    def increase_level(self):
        self.level += 1
        self.update_score()


    def game_over(self):

        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align="center")
