import colorgram
from turtle import Turtle, Screen
from random import choice

ROWS_OF_DOTS = 10
COLUMNS_OF_DOTS = 10
DOT_SIZE = 20
DOT_SPACING = 50
ORIGIN = (-250, -250)


def extract_colors(image_file, number_of_colors):
    """
    Uses the colorgram module to extract #number_of_colors from image_file and returns those colors in a tuple list.
    Ignores any colors that have an r, g & b above 220, don't want whites
    :param image_file:
    :param number_of_colors:
    :return:
    """
    colors = colorgram.extract(image_file, number_of_colors)
    rgbList = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        if r < 220 and g < 220 and b < 220:
            rgb = (r, g, b)
            rgbList.append(rgb)
    return rgbList


def draw_dots(turtle, origin_x, origin_y, colors, no_of_rows, no_of_cols, dot_size, space_between):
    """
    Draws a series of dots
    :param turtle:
    :param origin_x:
    :param origin_y:
    :param colors:
    :param no_of_rows:
    :param no_of_cols:
    :param dot_size:
    :param space_between:
    :return:
    """
    turtle.teleport(origin_x, origin_y)
    for row in range(no_of_rows):
        y = origin_y + (row * space_between)
        for col in range(no_of_cols):
            x = origin_x + (col * space_between)
            turtle.teleport(x, y)
            turtle.dot(dot_size, choice(colors))


turtle = Turtle()
turtle.speed(0)
screen = Screen()
screen.colormode(255)

colors = extract_colors('hirst-image.jpg', 50)

draw_dots(turtle, ORIGIN[0], ORIGIN[1], colors, ROWS_OF_DOTS, COLUMNS_OF_DOTS, DOT_SIZE, DOT_SPACING)

screen.exitonclick()

