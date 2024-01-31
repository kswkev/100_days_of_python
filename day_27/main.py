import tkinter

# Creating a window
window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)

# Creating a label
my_label = tkinter.Label(text="My Label", font=("Arial", 24, "bold"))
my_label.pack()

# Properties can be change by
# accessing them directly
my_label["text"] = "some new text"
# or thought the config method
my_label.config(text="more new text")

# Creating a button
button = tkinter.Button(text="Click Me")
button.pack()

def button_clicked():
    global my_label
    global input
    my_label["text"] = input.get()

button["command"] = button_clicked

input = tkinter.Entry(width=10)
input.pack()

window.mainloop()