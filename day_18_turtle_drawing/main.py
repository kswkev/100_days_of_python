from turtle import Turtle, Screen
from random import randint, choice

def set_random_color(turtle):
    colours = ["blue", "cyan", "brown", "gold", "green", "hotpink", "magenta", "maroon", "orange", "purple", "red"]
    turtle.pencolor(choice(colours))

def set_random_RGB_color(turtle):
    # turtle.colormode(255)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b)
    turtle.pencolor(rgb)

turtle = Turtle()
screen = Screen()
screen.colormode(255)

#draw a square
def draw_a_square(turtle, line_length):
    for _ in range(4):
        turtle.forward(line_length)
        turtle.right(90)


#draw a dashed line
def draw_dashed_line(turtle, dash_length, no_of_dashes):
    for _ in range(no_of_dashes):
        turtle.pendown()
        turtle.forward(dash_length)
        turtle.penup()
        turtle.forward(dash_length)


#drawing different shapes
def draw_different_shapes(turtle, no_of_shapes, line_length):
    for sides in range(3, no_of_shapes + 1):
        angle = 360 / sides
        set_random_color(turtle)
        for _ in range(sides):
            turtle.forward(line_length)
            turtle.right(angle)

def draw_random_walk(turtle, line_width, line_length, steps):
    turtle.speed(10)
    turtle.pensize(line_width)
    for _ in range(steps):
        # set_random_color(turtle)
        set_random_RGB_color(turtle)
        angle = 90 * randint(0, 4)
        turtle.setheading(angle)
        turtle.forward(line_length)

def draw_spirograph(turtle, radius, steps):
    turtle.speed(0)
    angle = int(360 / steps)
    for _ in range(steps):
        set_random_RGB_color(turtle)
        turtle.circle(radius)
        turtle.right(angle)




# draw_a_square(turtle, 100)
# draw_dashed_line(turtle, 10, 10)
# draw_different_shapes(turtle, 10, 100)
# draw_random_walk(turtle, 10, 30, 100)
draw_spirograph(turtle, 100, 90)

screen.exitonclick()
