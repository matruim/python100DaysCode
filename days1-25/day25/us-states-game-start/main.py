from turtle import Screen, Turtle, exitonclick
import pandas as pd
import tkinter as tk
from tkinter import messagebox


def confirm_exit():
    return messagebox.askyesno("Confirm", "Are you sure you want to quit the game?")


class USStatesGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.title("U.S. States Game")
        self.screen.setup(width=800, height=600)
        self.image = "blank_states_img.gif"
        self.screen.addshape(self.image)
        self.background_turtle = Turtle()
        self.background_turtle.shape(self.image)
        self.writing_turtle = Turtle()
        self.writing_turtle.penup()
        self.writing_turtle.hideturtle()
        self.states = pd.read_csv("50_states.csv")
        self.states_guessed = set()
        self.num_correct = 0

    def play(self):
        while self.num_correct < 50:
            answer_state = self.get_state_guess()
            if answer_state is None:
                if confirm_exit():
                    exit()
                else:
                    continue
            matched_state = self.check_state_guess(answer_state)
            if matched_state is not None:
                self.update_game_state(matched_state)
        exitonclick()

    def get_state_guess(self):
        state_input = self.screen.textinput(title=f"{self.num_correct}/50 States Correct",
                                            prompt="What's another state's name?")
        if state_input is not None:
            return state_input.lower()
        return None

    def check_state_guess(self, state_name):
        matched_states = self.states[self.states["state"].str.lower() == state_name]
        if not matched_states.empty:
            return matched_states.iloc[0]
        return None

    def update_game_state(self, state):
        if state["state"] in self.states_guessed:
            return
        self.num_correct += 1
        self.states_guessed.add(state["state"])
        self.write_state_on_map(state)

    def write_state_on_map(self, state):
        self.writing_turtle.goto(int(state["x"]), int(state["y"]))
        self.writing_turtle.write(state["state"], align="center", font=("Arial", 12, "normal"))


game = USStatesGame()
game.play()
