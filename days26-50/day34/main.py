import requests
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface


def start_game():
    url = "https://opentdb.com/api.php?amount=10&type=boolean"
    response = requests.get(url)
    response.raise_for_status()
    question_bank = [Question(question["question"], question["correct_answer"]) for question in
                     response.json()["results"]]
    return QuizBrain(question_bank)


quiz_brain = start_game()
QuizInterface(quiz_brain)
