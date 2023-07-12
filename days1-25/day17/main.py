from question_model import Question
from data import question_data, trivia_API_data
from quiz_brain import QuizBrain

# question_bank = [Question(question["text"], question["answer"]) for question in question_data]
question_bank = [Question(question["question"], question["correct_answer"]) for question in trivia_API_data]
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.final_score()