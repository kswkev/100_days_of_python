from turtle import Turtle

TURTLE_SHAPE = "square"
TURTLE_COLOR = "white"
TURTLE_SIZE = 20
RIGHT_HEADING = 0
UP_HEADING = 90
LEFT_HEADING = 180
DOWN_HEADING = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            x = 0 - (i * TURTLE_SIZE)
            self.add_segment((x, 0))

    def reset(self):
        for seg in self.segments:
            seg.goto(-1000,0)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape(TURTLE_SHAPE)
        new_segment.color(TURTLE_COLOR)
        new_segment.goto(position[0], position[1])
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(TURTLE_SIZE)

    def has_collided_with_tail(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def right(self):
        if self.head.heading() != LEFT_HEADING:
            self.head.setheading(RIGHT_HEADING)

    def up(self):
        if self.head.heading() != DOWN_HEADING:
            self.head.setheading(UP_HEADING)

    def left(self):
        if self.head.heading() != RIGHT_HEADING:
            self.head.setheading(LEFT_HEADING)

    def down(self):
        if self.head.heading() != UP_HEADING:
            self.head.setheading(DOWN_HEADING)
