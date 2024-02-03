from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

WINDOW_TITLE = "Password Manager"
IMG_FILE = "logo.png"
WEBSITE_TXT = "Website:"
USERNAME_TXT = "Email/Username:"
PASSWORD_TXT = "Password:"
SEARCH_TXT = "Search"
GENERATE_TXT = "Generate Password"
ADD_TXT = "Add"
DEFAULT_USERNAME = "kswkev@hotmail.com"
FONT = ("Ariel", 12, "bold")
WEBSITE_KEY = "Website"
USERNAME_KEY = "Username"
PASSWORD_KEY = "Password"
DATA_FILE_NAME = "data.json"
DELIMITER = "|"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    return password


def generate_and_populate_password():
    password_input.delete(0, END)
    password_input.insert(END, generate_password())


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    data_dict = load_from_file()

    try:
        entry = data_dict[website]
        username = entry[USERNAME_KEY]
        password = entry[PASSWORD_KEY]
    except KeyError:
        messagebox.showwarning(title="Website not found", message=f"No details for the website {website} exist")
    else:
        messagebox.showinfo(title="Account details", message=f"Website: {website}\n"
                                                             f"Email/Username: {username}\n"
                                                             f"Password: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    data_dict = {
        website: {
            USERNAME_KEY: username,
            PASSWORD_KEY: password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Validation Error", message="Please complete all boxes")
    else:
        message_text = (f"Is it ok to save the following data?\n"
                        f"Website: {website}\n"
                        f"Email/Username: {username}\n"
                        f"Password: {password}")
        is_ok = messagebox.askokcancel(title="Confirmation", message=message_text)
        if is_ok:
            existing_data = load_from_file()
            existing_data.update(data_dict)
            save_to_file(existing_data)
            reset_values()


def save_to_file(data_dict):
    with open(DATA_FILE_NAME, "w") as file:
        json.dump(data_dict, file, indent=4)


def load_from_file():
    try:
        with open(DATA_FILE_NAME, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open(DATA_FILE_NAME, "w") as file:
            json.dump({}, file, indent=4)
        with open(DATA_FILE_NAME, "r") as file:
            data = json.load(file)

    return data


def reset_values():
    website_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(WINDOW_TITLE)
window.config(padx=50, pady=50)

img = PhotoImage(file=IMG_FILE)
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text=WEBSITE_TXT, font=FONT)
website_label.grid(column=0, row=1)

website_input = Entry(width=21)
website_input.grid(column=1, row=1, sticky="w")
website_input.focus()

search_button = Button(text=SEARCH_TXT, width=10, command=find_password)
search_button.grid(column=2, row=1)

username_label = Label(text=USERNAME_TXT, font=FONT)
username_label.grid(column=0, row=2)

username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2, sticky="w")
username_input.insert(END, DEFAULT_USERNAME)

password_label = Label(text=PASSWORD_TXT, font=FONT)
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="w")

generate_button = Button(text=GENERATE_TXT, command=generate_and_populate_password)
generate_button.grid(column=2, row=3, sticky="w")

add_button = Button(text=ADD_TXT, width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
