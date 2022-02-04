# Trivia quiz game
# Quiz data generated from  https://www.opentdb.com/

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# initializing empty list of question bank objects
question_bank = []

# looping through question data and creating question objects
for question in question_data:
    current_question = Question(
        question_text=question["question"], question_answer=question["correct_answer"]
    )
    question_bank.append(current_question)

# initializing quiz brain object
quiz = QuizBrain(q_list=question_bank)

# looping through questions
while quiz.still_has_questions(total_questions=len(question_bank)):
    quiz.next_question()

# printing final score
print(f"You completed the quiz. Your final score was: {quiz.final_score()}\n")
