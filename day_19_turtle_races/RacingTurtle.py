from turtle import Turtle
import random


class RacingTurtle:

    def __init__(self, color, startingPos):
        self.turtle = Turtle("turtle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(startingPos[0], startingPos[1])

    def xcor(self):
        return self.turtle.xcor()

    def pencolor(self):
        return self.turtle.pencolor()

    def forward(self, distance):
        self.turtle.forward(distance)

    def forward_random_amount(self, min, max):
        movement = random.randint(min, max)
        self.forward(movement)