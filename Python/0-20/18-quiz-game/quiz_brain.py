class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # function to check if there are still questions left
    def still_has_questions(self, total_questions):
        return self.question_number < total_questions

    # function to move to next question
    def next_question(self):
        current_question = self.question_list[self.question_number]

        # incrementing question number
        self.question_number += 1

        # printing question
        valid_input = False
        while not valid_input:
            user_answer = input(
                f"Q.{self.question_number}: {current_question.text} (True/False?: "
            )
            if user_answer.lower() == "true" or user_answer.lower() == "false":
                valid_input = True
            else:
                print("Invalid Input. Try again")

        # checking answer
        self.check_answer(user_answer, current_question.answer)

    # function to check answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("That's wrong.")

        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    # function to print final score
    def final_score(self):
        return f"{self.score}/{self.question_number}"
