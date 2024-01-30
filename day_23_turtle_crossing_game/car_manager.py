from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
START_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1.1
AMOUNT_OF_STARTING_CARS = 50
CAR_SHAPE = "square"


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = START_MOVE_DISTANCE
        self.generate_cars(AMOUNT_OF_STARTING_CARS)

    def generate_cars(self, amount):
        for _ in range(amount):
            self.cars.append(self.generate_car())

    def generate_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape(CAR_SHAPE)
        new_car.turtlesize(stretch_wid=1, stretch_len=2)
        new_car.color(choice(COLORS))
        new_car.setheading(180)
        new_car.setpos(self.random_pos())
        return new_car

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)
            if car.xcor() <= -300:
                car.setpos(self.random_pos())

    def speed_up(self):
        self.car_speed *= MOVE_INCREMENT

    @staticmethod
    def random_pos():
        return (randint(0, 15) * 40) + 300, randint(-6, 6) * 40

    def collision(self, player):
        for car in self.cars:
            if car.distance(player) <= 30 and player.ycor() <= car.ycor() + 10 and player.ycor() >= car.ycor() - 10:
                return True
        return False