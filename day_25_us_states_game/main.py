import turtle
import pandas

STATES_IMAGE_FILE = "blank_states_img.gif"
POPUP_PROMPT = "What's another state name?"
POPUP_TITLE = "/50 States Correct"
DATA_FILE = "50_states.csv"

screen = turtle.Screen()
screen.title("US States Guessing Game")
screen.register_shape(STATES_IMAGE_FILE)
bk_turtle = turtle.Turtle()
bk_turtle.shape(STATES_IMAGE_FILE)
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

data = pandas.read_csv(DATA_FILE)
correct_guesses = []
all_states = data.state.to_list()

while True:
    states_guess = screen.textinput(title=f"{len(correct_guesses)}{POPUP_TITLE}", prompt=POPUP_PROMPT).title()
    if states_guess not in correct_guesses and states_guess in all_states:
        correct_guesses.append(states_guess)
        row = data[data.state == states_guess]
        pos = (int(row.x), int(row.y))
        writer.goto(pos)
        writer.write(f"{row.state.item()}", move=False, align="center", font=('Courier', 8, 'normal'))

    if states_guess == "Exit":
        missing_states = [state for state in all_states if state not in correct_guesses]
        missing_data = pandas.DataFrame(missing_states)
        missing_data.to_csv("states_to_learn.csv")
        break

# screen.mainloop()