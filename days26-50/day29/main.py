from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open("data.txt", mode='a') as data_file:
        data_file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.insert(END, "matruim")

# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas setup
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels setup
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_label.grid(column=0, row=1, sticky='e')
email_label.grid(column=0, row=2, sticky='e')
password_label.grid(column=0, row=3, sticky='e')

# Inputs setup
website_entry = Entry(width=35)
email_entry = Entry(width=35)
password_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=2, sticky='w')
email_entry.grid(column=1, row=2, columnspan=2, sticky='w')
password_entry.grid(column=1, row=3, columnspan=1, sticky='w')
website_entry.focus()
email_entry.insert(END, "matruim")

# Buttons setup
gen_pass_btn = Button(text="Generate Password")
add_btn = Button(text="Add", width=36, command=save_password)
gen_pass_btn.grid(column=2, row=3)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
