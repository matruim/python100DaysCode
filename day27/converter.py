from tkinter import *

FONT = ("Arial", 20, "normal")


def convert_to_km():
    km = float(user_input.get()) * 1.609344
    answer_label.config(text=round(km, 2))


def convert_to_miles():
    miles = float(user_input.get()) / 1.609344
    answer_label.config(text=round(miles, 2))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=320, height=240)
window.config(padx=10, pady=10)

user_input = Entry(width=10)
user_input.grid(column=1, row=0)

calculate_button = Button(text="Calculate", command=convert_to_miles)
calculate_button.grid(column=1, row=2)

userinput_label = Label(text="Km", font=FONT)
userinput_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)

answer_label = Label(text="", font=FONT)
answer_label.grid(column=1, row=1)

converted_label = Label(text="Miles", font=FONT)
converted_label.grid(column=2, row=1)

window.mainloop()
