from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TOP = int((SCREEN_HEIGHT / 2) - 20)
SCREEN_BOTTOM = int(-1 * ((SCREEN_HEIGHT / 2) - 20))
SCREEN_RIGHT_SIDE = SCREEN_WIDTH / 2
SCREEN_LEFT_SIDE = -1 * (SCREEN_WIDTH / 2)
SCREEN_COLOR = "Black"
SCREEN_TITLE = "Pong"

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.title(SCREEN_TITLE)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() <= SCREEN_BOTTOM or ball.ycor() >= SCREEN_TOP:
        ball.y_bounce()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.x_bounce()

    if ball.xcor() >= SCREEN_RIGHT_SIDE:
        scoreboard.l_point()
        ball.return_to_start()

    if ball.xcor() <= SCREEN_LEFT_SIDE:
        scoreboard.r_point()
        ball.return_to_start()

screen.exitonclick()