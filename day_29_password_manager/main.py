from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

WINDOW_TITLE = "Password Manager"
IMG_FILE = "logo.png"
WEBSITE_TXT = "Website:"
USERNAME_TXT = "Email/Username:"
PASSWORD_TXT = "Password:"
GENERATE_TXT = "Generate Password"
ADD_TXT = "Add"
DEFAULT_USERNAME = "kswkev@hotmail.com"
FONT = ("Ariel", 12, "bold")
WEBSITE_KEY = "Website"
USERNAME_KEY = "Username"
PASSWORD_KEY = "Password"
DATA_FILE_NAME = "data.txt"
DELIMITER = "|"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    data_dict = {
        WEBSITE_KEY: website_input.get(),
        USERNAME_KEY: username_input.get(),
        PASSWORD_KEY: password_input.get()
    }

    if len(data_dict[WEBSITE_KEY]) == 0 or len(data_dict[USERNAME_KEY]) == 0 or len(data_dict[PASSWORD_KEY]) == 0:
        messagebox.showerror(title="Valatation Error", message="Please complete all boxes")
    else:
        message_text = (f"Is it ok to save the following data?\n"
                        f"Website: {data_dict[WEBSITE_KEY]}\n"
                        f"Email/Username: {data_dict[USERNAME_KEY]}\n"
                        f"Password: {data_dict[PASSWORD_KEY]}")
        is_ok = messagebox.askokcancel(title="Confirmation", message=message_text)
        if is_ok:
            save_to_file(data_dict)
            reset_values()


def save_to_file(data_dict):
    with open(DATA_FILE_NAME, "a") as file:
        file.write(f"{data_dict[WEBSITE_KEY]}{DELIMITER}{data_dict[USERNAME_KEY]}{DELIMITER}{data_dict[PASSWORD_KEY]}\n")


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

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="w")
website_input.focus()

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
