from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.bounce_y()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        if self.xcor() > 320 and self.x_move == abs(self.x_move):
            self.x_move *= -1
            self.move_speed *= 0.9

        if self.xcor() < -320 and self.x_move == -abs(self.x_move):
            self.x_move *= -1
            self.move_speed *= 0.9


    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1