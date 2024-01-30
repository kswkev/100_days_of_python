from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def turn_left():
    turtle.left(10)


def turn_right():
    turtle.right(10)


def clear():
    turtle.penup()
    turtle.home()
    turtle.clear()
    turtle.pendown()


commands = {"w": move_forward,
            "s": move_backward,
            "a": turn_left,
            "d": turn_right,
            "c": clear, }


screen.listen()
for key in commands:
    screen.onkey(key=key, fun=commands[key])

screen.exitonclick()