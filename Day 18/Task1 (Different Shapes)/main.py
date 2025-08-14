from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.width(3)
screen = Screen()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


for i in range(3,11):
    tim.color(random.choice(colours))
    for j in range(1,i+1):
        tim.forward(100)
        tim.right(180-(i-2)*180/i)

screen.exitonclick()