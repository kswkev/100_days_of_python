from turtle import Turtle

SHAPE = "circle"
COLOR = "White"

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.setheading(45)
        self.color(COLOR)
        self.penup()
        self.x_velocity = 10
        self.y_velocity = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_velocity
        new_y = self.ycor() + self.y_velocity
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_velocity *= -1

    def x_bounce(self):
        self.x_velocity *= -1
        self.move_speed *= 0.9

    def return_to_start(self):
        self.goto(0, 0)
        self.x_bounce()
        self.move_speed = 0.1
