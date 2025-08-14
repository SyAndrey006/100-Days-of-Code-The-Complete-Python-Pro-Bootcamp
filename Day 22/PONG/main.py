from time import sleep
from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))
screen.update()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")

screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")

game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.distance(paddle_l) < 50 and ball.xcor() < -320 or ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_score_l()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_score_r()

screen.exitonclick()