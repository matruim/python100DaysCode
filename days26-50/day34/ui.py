from tkinter import Tk, Canvas, Button, PhotoImage, Label
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


def create_button(text, command, row, column):
    button = Button(text=text, command=command)
    button.grid(row=row, column=column)
    return button


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lbl = Label(
            text="Score: 0",
            bg=THEME_COLOR,
            font=("Arial", 16, "normal"),
            fg="white"
        )

        self.canvas = Canvas(
            width=300,
            height=240,
            bg="white",
        )
        self.question_text = self.canvas.create_text(
            150,
            120,
            text=self.quiz_brain.question_text(),
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=280
        )

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_btn = Button(image=true_image, command=lambda: self.check_answer(True))
        self.false_btn = Button(image=false_image, command=lambda: self.check_answer(False))

        self.score_lbl.grid(row=0, column=1, )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.true_btn.grid(row=2, column=0)
        self.false_btn.grid(row=2, column=1)

        self.window.mainloop()

    def flash_color(self, color, delay_ms, num_flashes=2):
        self.canvas.config(bg=color)
        num_flashes -= 1

        if num_flashes > 0:
            self.canvas.after(delay_ms, self.flash_color, THEME_COLOR, delay_ms, num_flashes)
        else:
            self.canvas.config(bg="white")
            self.get_next_question()

    def update_question(self, q_text):
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.score_lbl.config(text=f"Score: {self.quiz_brain.score}")

    def check_answer(self, answer):
        self.flash_color("green", 500) if self.quiz_brain.is_correct_answer(answer) else self.flash_color("red", 500)

    def get_next_question(self):
        if self.quiz_brain.still_has_questions():
            self.quiz_brain.next_question()
            self.update_question(self.quiz_brain.question_text())
        else:
            self.update_question(self.quiz_brain.final_score())
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
