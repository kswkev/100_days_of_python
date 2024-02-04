from tkinter import *
from random import choice
import pandas

DATA_FILE = "data/french_words.csv"
WORDS_TO_LEARN_FILE = "data/words_to_learn.csv"
CARD_BACK_IMAGE = "images/card_back.png"
CARD_FRONT_IMAGE = "images/card_front.png"
RIGHT_IMAGE = "images/right.png"
WRONG_IMAGE = "images/wrong.png"

BACKGROUND_COLOR = "#B1DDC6"
WINDOW_TITLE = "Flash Cards"
WINDOW_PADDING = 50
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 526
CARD_XPOS = CANVAS_WIDTH/2
CARD_YPOS = CANVAS_HEIGHT/2
SOURCE_LANGUAGE = "French"
TARGET_LANGUAGE = "English"
LANGUAGE_XPOS = (CANVAS_WIDTH/2)
LANGUAGE_YPOS = (CANVAS_HEIGHT/2)-113
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_XPOS = (CANVAS_WIDTH/2)
WORD_YPOS = (CANVAS_HEIGHT/2)+50
WORD_FONT = ("Ariel", 60, "bold")
FRONT_TEXT_COLOUR = "black"
BACK_TEXT_COLOUR = "white"
FLIP_TIME = 3000
to_learn = {}
current_card = {}
flip_timer = None


# ----------------------------- DATA DICTIONARY ----------------------
def populate_dictionary():
    global to_learn
    try:
        data = pandas.read_csv(WORDS_TO_LEARN_FILE)
    except FileNotFoundError:
        original_data = pandas.read_csv(DATA_FILE)
        to_learn = original_data.to_csv(WORDS_TO_LEARN_FILE)
    else:
        to_learn = data.to_dict(orient="records")


# ----------------------------- RANDOM WORD -------------------------
def fetch_random():
    global to_learn
    return choice(to_learn)


def next_card():
    global current_card, flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    current_card = fetch_random()
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text=SOURCE_LANGUAGE, fill=FRONT_TEXT_COLOUR)
    canvas.itemconfig(card_word, text=current_card[SOURCE_LANGUAGE], fill=FRONT_TEXT_COLOUR)
    flip_timer = window.after(FLIP_TIME, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text=TARGET_LANGUAGE, fill=BACK_TEXT_COLOUR)
    canvas.itemconfig(card_word, text=current_card[TARGET_LANGUAGE], fill=BACK_TEXT_COLOUR)


# ----------------------------- REMOVE LEARNED WORD ------------------
def is_known():
    global to_learn
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(WORDS_TO_LEARN_FILE)
    next_card()


# ----------------------------- UI -----------------------------------
window = Tk()
window.title(WINDOW_TITLE)
window.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING, bg=BACKGROUND_COLOR)

card_back_img = PhotoImage(file=CARD_BACK_IMAGE)

canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

card_front_img = PhotoImage(file=CARD_FRONT_IMAGE)
card_back_img = PhotoImage(file=CARD_BACK_IMAGE)
canvas_image = canvas.create_image(CARD_XPOS, CARD_YPOS, image=card_front_img)

card_title = canvas.create_text(LANGUAGE_XPOS, LANGUAGE_YPOS, text="language", font=LANGUAGE_FONT)
card_word = canvas.create_text(WORD_XPOS, WORD_YPOS, text="word", font=WORD_FONT)

wrong_img = PhotoImage(file=WRONG_IMAGE)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file=RIGHT_IMAGE)
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)


# ---------------------------- SETUP CARD -------------------------------
populate_dictionary()
next_card()


window.mainloop()
