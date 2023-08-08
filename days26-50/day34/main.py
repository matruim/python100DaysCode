import requests
from tkinter import Tk, Canvas, Button
from question_model import Question
from quiz_brain import QuizBrain


def initialize_gui():
    win = Tk()
    win.title("Quiz Time")
    win.config(padx=50, pady=50)

    c = Canvas(width=600, height=414)
    qt = c.create_text(260, 207, text="", width=500, font=("Arial", 30, "bold"), fill="black")
    c.grid(row=0, column=0, columnspan=2)

    true_btn = create_button("True", lambda: check_answer(True), row=1, column=0)
    false_btn = create_button("False", lambda: check_answer(False), row=1, column=1)

    return win, c, true_btn, false_btn, qt, c.cget("bg")


def create_button(text, command, row, column):
    button = Button(text=text, command=command)
    button.grid(row=row, column=column)
    return button


def flash_color(color, delay_ms, num_flashes=2):
    canvas.config(bg=color)
    num_flashes -= 1

    if num_flashes > 0:
        canvas.after(delay_ms, flash_color, original_bg_color, delay_ms, num_flashes)
    else:
        canvas.config(bg=original_bg_color)
        next_question()


def check_answer(answer):
    flash_color("green", 500) if quiz_brain.is_correct_answer(answer) else flash_color("red", 500)


def next_question():
    if quiz_brain.still_has_questions():
        quiz_brain.next_question()
        canvas.itemconfig(question_text, text=quiz_brain.question_text())
    else:
        canvas.itemconfig(question_text, text=quiz_brain.final_score())
        true_button.config(state="disabled")
        false_button.config(state="disabled")


def start_game():
    url = "https://opentdb.com/api.php?amount=10&type=boolean"
    response = requests.get(url)
    response.raise_for_status()
    question_bank = [Question(question["question"], question["correct_answer"]) for question in
                     response.json()["results"]]
    return QuizBrain(question_bank)


window, canvas, true_button, false_button, question_text, original_bg_color = initialize_gui()
quiz_brain = start_game()
canvas.itemconfig(question_text, text=quiz_brain.question_text())

window.mainloop()
