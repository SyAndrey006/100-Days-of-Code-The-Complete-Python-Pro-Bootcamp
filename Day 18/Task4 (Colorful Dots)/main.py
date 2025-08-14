from turtle import Turtle, Screen
import random, turtle
tim = Turtle()
tim.shape("turtle")
tim.width(1)
tim.speed("fastest")
screen = Screen()
turtle.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

tim.penup()

for i in range(-200,201,10):
    for j in range(-200,201,10):
        tim.setpos(j,i)
        tim.pendown()
        tim.dot(5, random_colour())
        tim.penup()

screen.exitonclick()