import random
import tkinter as tk
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
words = {"French": {}, "English": {}}
word = 0
rotate = None


def load_words():
    global words
    try:
        csv = pd.read_csv("data/words_to_learn.csv")
        words = csv.to_dict()
    except FileNotFoundError:
        csv = pd.read_csv("data/french_words.csv")
        words = csv.to_dict()

    if len(words["French"]) < 1:
        csv = pd.read_csv("data/french_words.csv")
        words = csv.to_dict()


def save_words():
    global words
    pd.DataFrame(words).to_csv("data/words_to_learn.csv", index=False)


def wrong_answer():
    window.after_cancel(rotate)
    load_word()


def right_answer():
    global words, rotate
    words["French"].pop(word)
    words["English"].pop(word)
    window.after_cancel(rotate)
    save_words()
    load_word()


def flip_card(english_word):
    canvas.itemconfig(canvas_image, image=card_bg)
    canvas.itemconfig(word_label, text=english_word)


def load_word():
    global word, rotate
    canvas.itemconfig(canvas_image, image=card_fg)
    word = random.choice(list(words["French"]))
    canvas.itemconfig(word_label, text=words["French"][word])
    rotate = window.after(3000, flip_card, words["English"][word])


def startup():
    load_words()
    load_word()


# Window setup
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas setup
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_bg = tk.PhotoImage(file="images/card_back.png")
card_fg = tk.PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_fg)
language_label = canvas.create_text(400, 100, text="French", fill="black", font=("Arial", 35, "italic"))
word_label = canvas.create_text(400, 240, text="Word", fill="black", font=("Arial", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button setup
no_image = tk.PhotoImage(file="images/wrong.png")
yes_image = tk.PhotoImage(file="images/right.png")
no_btn = tk.Button(image=no_image, highlightthickness=0, command=wrong_answer)
yes_btn = tk.Button(image=yes_image, highlightthickness=0, command=right_answer)
no_btn.grid(column=0, row=1)
yes_btn.grid(column=1, row=1)

startup()

window.mainloop()
