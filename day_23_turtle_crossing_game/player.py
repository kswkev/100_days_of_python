from turtle import Turtle

PLAYER_SHAPE = "turtle"
STARTING_POS = (0, -280)
MOVEMENT_RATE = 10
FINISHING_LINE = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(PLAYER_SHAPE)
        self.penup()
        self.goto(STARTING_POS)
        self.setheading(90)

    def move(self):
        self.forward(MOVEMENT_RATE)

    def return_to_start(self):
        self.goto(STARTING_POS)

    def passed_finishing_line(self):
        return self.ycor() >= FINISHING_LINE
