from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title = "Make your bet" , prompt = "Which turtle will win the race? Choose a color: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "navy" , "purple"]
y_position = [-90, -60, -30, 0, 30, 60, 90]
turtle_list = []

for turtle_index in range(0,6):
    turtle = Turtle(shape = "turtle",)
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x = -240, y = y_position[turtle_index])
    turtle_list.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()