import random
# this art package is from https://github.com/sepandhaghighi/art#font-modes
from art import *

NUMBER_RANGE = (1, 100)
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
DIFFICULTY_PROMPT = "Choose a difficulty. Type 'easy' or 'hard': "
PROMPT_DECORATIONS = {'tarty1': 'GUESS THE NUMBER', 'fancy92': 'To high, try a lower number',
                      'sad1': 'You\'ve run out of guesses, you lose.'}

def get_difficulty():
    while True:
        difficulty = input(text2art(DIFFICULTY_PROMPT))
        if difficulty in ['easy', 'hard']:
            return difficulty


def play_game():
    number_to_guess = random.randint(*NUMBER_RANGE)
    tprint(PROMPT_DECORATIONS["tarty1"], font="tarty1")
    difficulty = get_difficulty()
    attempts = EASY_ATTEMPTS if difficulty == 'easy' else HARD_ATTEMPTS
    tprint(f'I\'m thinking of a number between {NUMBER_RANGE[0]} and {NUMBER_RANGE[1]}.')
    tprint(f'You have {attempts} attempts remaining to guess the number.')

    while attempts > 0:
        guess = int(input(text2art("Pick a number between 1 and 100: ")))
        if guess == number_to_guess:
            tprint("You guessed it", decoration="champion1")
            return
        elif guess > number_to_guess:
            decoration = 'fancy92'
        else:
            decoration = 'fancy92'

        attempts -= 1
        if attempts > 0:
            tprint(f'You have {attempts} attempts remaining to guess the number.')
        else:
            decoration = 'sad1'

        tprint(PROMPT_DECORATIONS[decoration], decoration=decoration)





if __name__ == '__main__':
    set_default(font='fancy91')
    play_game()
