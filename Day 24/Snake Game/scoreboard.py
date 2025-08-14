from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score = 0
        with open("highest_score.txt") as data:
            self.highest_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | {self.highest_score}", align="center", font=("Courier", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Courier", 20, "normal"))

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest_score.txt", mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()
