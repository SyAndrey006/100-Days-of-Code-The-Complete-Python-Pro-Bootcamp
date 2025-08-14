from turtle import Turtle
from collections import deque

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []

        self.create_snake()
        self.head = self.segments[0]
        self.direction_queue = deque()

    def create_snake(self):
        for position in STARTING_POSITION:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.segments.append(segment)

    def extend(self):
        self.segments.append(Turtle("square"))
        self.segments[-1].color("white")
        self.segments[-1].penup()
        last_segment = self.segments[-2]
        self.segments[-1].goto(last_segment.position())

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.direction_queue.clear()

    def move(self):

        if self.direction_queue:
            self.head.setheading(self.direction_queue.popleft())

        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)

        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            print(self.head.heading())
            self.direction_queue.append(90)

    def down(self):
        if self.head.heading() != 90:
            print(self.head.heading())
            self.direction_queue.append(270)

    def left(self):
        if self.head.heading() != 0:
            print(self.head.heading())
            self.direction_queue.append(180)

    def right(self):
        if self.head.heading() != 180:
            print(self.head.heading())
            self.direction_queue.append(0)

