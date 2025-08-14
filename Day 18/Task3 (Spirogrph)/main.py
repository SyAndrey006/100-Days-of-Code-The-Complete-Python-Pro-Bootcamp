from turtle import Turtle, Screen
import random, turtle
tim = Turtle()
tim.shape("turtle")
tim.width(2)
tim.speed("fastest")
screen = Screen()
turtle.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

for i in range(36):
    tim.pencolor(random_colour())
    tim.circle(100)
    tim.left(10)

screen.exitonclick()
