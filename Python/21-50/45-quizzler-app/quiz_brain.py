import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """ Checks if there are still questions left in the list and returns True if so """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """ Moves to the next question """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        # converting the html text to plain text
        question_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {question_text} (True/False): "
    
        # user_answer = input(f"Q.{self.question_number}: {question_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer) -> bool:
        """ Checks the answer and returns True and updates Score if it is correct """
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False
