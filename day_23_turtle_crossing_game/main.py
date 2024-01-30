import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Turtle Crossing"
SLEEP_TIME = 0.1

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title(SCREEN_TITLE)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_on = True
while game_on:
    time.sleep(SLEEP_TIME)
    car_manager.move_cars()

    if player.passed_finishing_line():
        player.return_to_start()
        scoreboard.point()
        car_manager.speed_up()

    if car_manager.collision(player):
        game_on = False
        scoreboard.game_over()

    screen.update()

screen.exitonclick()
