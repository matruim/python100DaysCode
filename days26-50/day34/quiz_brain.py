from question_model import Question


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = self.question_list[self.question_number]

    def next_question(self):
        self.question_number += 1
        self.current_question = self.question_list[self.question_number]

    def still_has_questions(self):
        return self.question_number < len(self.question_list)-1

    def final_score(self):
        return f"Your final score was: {self.score}/{self.question_number+1}"

    def question_text(self):
        return self.question_list[self.question_number].text

    def is_correct_answer(self, user_answer) -> bool:
        correct_answer = bool(self.question_list[self.question_number].answer == "True")
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False
