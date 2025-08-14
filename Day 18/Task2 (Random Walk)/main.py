from turtle import Turtle, Screen
import random, turtle
tim = Turtle()
tim.shape("turtle")
# tim.color("green")
tim.width(20)
tim.speed("fastest")
screen = Screen()
turtle.colormode(255)

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

for i in range(1000):
    # tim.color(random.choice(colours))
    tim.pencolor(random_colour())
    tim.forward(35)
    tim.setheading(random.choice(directions))