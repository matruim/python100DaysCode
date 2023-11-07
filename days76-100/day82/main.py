import pandas as pd
from playsound import playsound
import time

def load_morse_code_dictionary(file_path):
    morse_data = pd.read_csv(file_path)
    return {row.letter: row.code for _, row in morse_data.iterrows()}

def translate_to_morse_code(message, morse_dic):
    message = message.upper()
    morse_code = ' '.join([morse_dic.get(letter, '') if letter != ' ' else ' ' for letter in message])
    print(morse_code)
    return morse_code

def play_morse_code(code):
    sound_files = {'.': 'dot.wav', '-': 'dash.wav', ' ': None}
    for symbol in code:
        if symbol == ' ':
            time.sleep(0.25)  # Pause between letters
        elif symbol in sound_files:
            playsound(sound_files[symbol])
            time.sleep(0.05)

if __name__ == '__main__':
    morse_dic = load_morse_code_dictionary("morse_code.csv")
    message = input("Enter a message to translate: ")
    morse_code = translate_to_morse_code(message, morse_dic)
    play_morse_code(morse_code)
