import art
from replit import clear
from game_data import data
from random import choice


def print_logo():
    print(art.logo)


def print_vs():
    print(art.vs)


def return_random_entry():
    return choice(data)


def get_data_string(data_for):
    return f"{data_for['name']}, a {data_for['description']}, from {data_for['country']}."


def print_A_Details(data_for):
    print("Compare A: " + get_data_string(data_for))


def print_B_Details(data_for):
    print("Against B: " + get_data_string(data_for))


def print_Comparison_text(data_for_A, data_for_B):
    print_A_Details(data_for_A)
    print_vs()
    print_B_Details(data_for_B)


def compair(a_followers, b_followers):
    if a_followers > b_followers:
        return "A"
    else:
        return "B"


def run_game():
    score = 0
    continue_game = True

    data_for_A = return_random_entry()

    while continue_game:
        clear()
        print_logo()

        data_for_B = return_random_entry()

        print_Comparison_text(data_for_A, data_for_B)
        guess = input("Who has more followers? 'A' or 'B': ")

        answer = compair(data_for_A["follower_count"], data_for_B["follower_count"])

        if guess == answer:
            print(
                f"Correct! {data_for_A['name']} has {data_for_A['follower_count']} followers, while {data_for_B['name']} has {data_for_B['follower_count']} followers")
            score += 1
        else:
            print(
                f"Incorrect! {data_for_A['name']} has {data_for_A['follower_count']} followers, while {data_for_B['name']} has {data_for_B['follower_count']} followers")
            print(f"Final score: {score}")
            continue_game = False

        if answer == "B":
            data_for_A = data_for_B


run_game()