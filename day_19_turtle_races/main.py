from turtle import Screen
from Race import Race

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 400
TURTLE_STARTING_Y = -100
Y_DISTANCE_BETWEEN_TURTLES = 40
X_START_OFFSET = 20

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

screen_left_edge = (SCREEN_WIDTH / 2) * -1
screen_right_edge = (SCREEN_WIDTH / 2)

race = Race(colors, screen_left_edge + X_START_OFFSET, TURTLE_STARTING_Y, Y_DISTANCE_BETWEEN_TURTLES, screen_right_edge)

user_bet = screen.textinput("Enter your bet", "Which turtle will win the race, enter a color: ").lower()

winner = ""
if user_bet:
    winner = race.startRace()

print(f"Winner: {winner}")
if user_bet == winner:
    print("You win!")
else:
    print("You loose.")

screen.exitonclick()