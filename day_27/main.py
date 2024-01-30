import tkinter

# Creating a window
window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)

# Creating a label
my_label = tkinter.Label(text="My Label", font=("Arial", 24, "bold"))
my_label.pack()

window.mainloop()