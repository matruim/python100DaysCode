import random
import string
import pyperclip
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    length = random.randint(8, 16)
    password_entry.delete(0, END)
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure at least one of each required character type
    password = [random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase),
                random.choice(string.digits), random.choice(string.punctuation)]

    # Fill the remaining password length with random characters
    password.extend(random.choice(characters) for _ in range(length))

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    password_str =  ''.join(str(char) for char in password)
    password_entry.insert(END, password_str)
    pyperclip.copy(password_str)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                          f"\nPassword: {password} \nIs it ok to save?")
    if is_ok:
        with open("data.txt", mode='a') as data_file:
            data_file.write(f"{website} | {email} | {password}\n")

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
gen_pass_btn = Button(text="Generate Password", command=generate_password)
add_btn = Button(text="Add", width=36, command=save_password)
gen_pass_btn.grid(column=2, row=3)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
