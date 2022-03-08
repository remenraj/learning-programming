from tkinter import *
from quiz_brain import QuizBrain


# file directories
TRUE_IMG_DIR = r"learning-programming\Python\21-50\45-quizzler-app\images\true.png"
FALSE_IMG_DIR = r"learning-programming\Python\21-50\45-quizzler-app\images\false.png"

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # quiz_brain is a QuizBrain object
        self.quiz = quiz_brain
        # setting up screen
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # score label
        self.score_label = Label(text="Score: 0/0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, padx=5, pady=5)

        # question canvas
        self.question_canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.question_canvas.create_text(
            150,
            125,
            width=280,
            text="dd",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
        )
        self.question_canvas.grid(row=1, column=0, padx=5, pady=20, columnspan=2)

        # setting up buttons
        try:
            correct_button_img = PhotoImage(file=TRUE_IMG_DIR)
        except FileNotFoundError:
            print("Could not find the image file")
        else:
            self.correct_button = Button(
                image=correct_button_img,
                highlightthickness=0,
                bg=THEME_COLOR,
                command=self.correct_answer,
            )
            self.correct_button.grid(row=2, column=0, padx=5, pady=5)
        try:
            wrong_button_img = PhotoImage(file=FALSE_IMG_DIR)
        except FileNotFoundError:
            print("Could not find image file")
        else:
            self.wrong_button = Button(
                image=wrong_button_img,
                highlightthickness=0,
                bg=THEME_COLOR,
                command=self.wrong_answer,
            )
            self.wrong_button.grid(row=2, column=1, padx=5, pady=5)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="white")
        self.score_label.config(
            text=f"Score: {self.quiz.score}/{self.quiz.question_number}"
        )
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            self.question_canvas.itemconfig(
                self.question_text,
                text=f"You have finished the quiz!\nYour final score is: {self.quiz.score}/{self.quiz.question_number}",
            )

    def wrong_answer(self):
        # When the user clicks the wrong button, this function is called.
        # This function calls the check_answer function in the quiz_brain class and passes the user's answer as "False"
        # The feedback function is called and the score is updated
        self.feedback(self.quiz.check_answer("False"))

    def correct_answer(self):
        # When the user clicks the correct button, this function is called.
        # This function calls the check_answer function in the quiz_brain class and passes the user's answer as "True"
        # The feedback function is called and the score is updated
        self.feedback(self.quiz.check_answer("True"))

    def feedback(self, answer: bool):
        if answer:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")

        # showing the next question after half a second
        self.window.after(500, self.get_next_question)
