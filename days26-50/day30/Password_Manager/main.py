import random
import string
import pyperclip
import json
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
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty!")
        return

    else:
        try:
            with open("data.json", mode='r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", mode='w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.insert(END, "matruim")


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_websites():
    website = website_entry.get()
    try:
        with open("data.json", mode='r') as data_file:
            data = json.load(data_file)
    except KeyError as message:
        messagebox.showinfo(title="Oops", message=f"Website {message} has no entry.")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message=f"No entries have been recorded.")
    else:
        messagebox.showinfo(title=f"{website}", message=f"{website} \nUsername: {data[website]['email']} \nPassword: {data[website]['password']}")


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
website_entry = Entry(width=24)
email_entry = Entry(width=40)
password_entry = Entry(width=24)
website_entry.grid(column=1, row=1, sticky='w')
email_entry.grid(column=1, row=2, columnspan=2, sticky='w')
password_entry.grid(column=1, row=3, sticky='w')
website_entry.focus()
email_entry.insert(END, "matruim")

# Buttons setup
gen_pass_btn = Button(text="Generate Password", command=generate_password, width=12)
add_btn = Button(text="Add", width=36, command=save_password)
search_btn = Button(text="Search", command=search_websites, width=12)
gen_pass_btn.grid(column=2, row=3)
add_btn.grid(column=1, row=4, columnspan=2)
search_btn.grid(column=2, row=1)

window.mainloop()
