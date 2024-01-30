from turtle import Turtle

SHAPE = "square"
COLOR = "White"
SPEED = 20

class Paddle(Turtle):

    def __init__(self, starting_pos):
        super().__init__()
        self.shape(SHAPE)
        self.setheading(90)
        self.color(COLOR)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(starting_pos)

    def move_up(self):
        new_y = self.ycor() + SPEED
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - SPEED
        self.goto(self.xcor(), new_y)
