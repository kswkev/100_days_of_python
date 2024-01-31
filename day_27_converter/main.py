from tkinter import *


def convert_to_km(miles):
    return round(float(miles) * 1.609, 2)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=15)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equals_label = Label(text="is equal to")
equals_label.grid(column=0, row=1)

value_label = Label(text="0")
value_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


def update_km():
    global miles_input
    global value_label
    miles = miles_input.get()
    km = convert_to_km(miles)
    value_label.config(text=f"{km}")


calculate_button = Button(text="Calculate")
calculate_button.grid(column=1, row=2)
calculate_button.config(command=update_km)

window.mainloop()