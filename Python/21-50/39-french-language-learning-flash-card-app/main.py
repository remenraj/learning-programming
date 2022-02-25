# French language learning flash card app
# Program will show a random french word from a list of words to learn and after 3 seconds it will flip the card over and show the english word
from tkinter import *
import pandas, random


# file directories
try:
    CARD_BACK_DIR = r"learning-programming\Python\21-50\39-french-language-learning-flash-card-app\images\card_back.png"
    CARD_FRONT_DIR = r"learning-programming\Python\21-50\39-french-language-learning-flash-card-app\images\card_front.png"
    RIGHT_DIR = r"learning-programming\Python\21-50\39-french-language-learning-flash-card-app\images\right.png"
    WRONG_DIR = r"learning-programming\Python\21-50\39-french-language-learning-flash-card-app\images\wrong.png"
    FRENCH_WORDS_DIR = r"learning-programming\Python\21-50\39-french-language-learning-flash-card-app\data\french_words.csv"
    WORDS_TO_LEARN_DIR = r"learning-programming\Python\21-50\39-french-language-learning-flash-card-app\data\words_to_learn.csv"
except FileNotFoundError:
    print("File not found")


# ---------------------------- NEW FLASH CARD SETUP ------------------------------- #

# creating dataframe
try:
    french_data_df = pandas.read_csv(WORDS_TO_LEARN_DIR)
except FileNotFoundError:
    french_data_df = pandas.read_csv(FRENCH_WORDS_DIR)

# converting dataframe into a list containing dictionary of each row
french_data = french_data_df.to_dict(orient="records")

# creating empty dictionary for current card
current_card = {}


def correct_answer():
    """Removes the current card from the list of words to learn"""
    global current_card, flip_timer
    # cancelling the timer
    window.after_cancel(flip_timer)

    canvas.itemconfig(canvas_image, image=card_front_img)
    current_card = random.choice(french_data)

    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=current_card["French"])

    french_data.remove(current_card)

    flip_timer = window.after(ms=3000, func=flip_card)

    # creating a csv file containing words to learn, known words are removed
    words_to_learn = pandas.DataFrame(data=french_data)
    words_to_learn.to_csv(WORDS_TO_LEARN_DIR, index=False)


def wrong_answer():
    """Shows"""
    global current_card, flip_timer
    # cancelling the timer
    window.after_cancel(flip_timer)

    canvas.itemconfig(canvas_image, image=card_front_img)
    current_card = random.choice(french_data)

    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=current_card["French"])

    flip_timer = window.after(ms=3000, func=flip_card)


# ---------------------------- FLIP CARD ------------------------------- #


def flip_card():
    """Flips the card over"""
    canvas.itemconfig(canvas_image, image=card_back_img)

    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=current_card["English"])


# ---------------------------- UI SETUP ------------------------------- #

# background color
BACKGROUND_COLOR = "#B1DDC6"

# setting up screen
window = Tk()
window.title("Flashy")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)
flip_timer = window.after(ms=3000, func=flip_card)

# setting up background image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=CARD_FRONT_DIR)
card_back_img = PhotoImage(file=CARD_BACK_DIR)
canvas_image = canvas.create_image(400, 263, image=card_front_img)


title_text = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

# setting up buttons
wrong_button_img = PhotoImage(file=WRONG_DIR)
wrong_button = Button(
    image=wrong_button_img,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    command=wrong_answer,
)
wrong_button.grid(row=1, column=0, padx=5, pady=5)

right_button_img = PhotoImage(file=RIGHT_DIR)
right_button = Button(
    image=right_button_img,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    command=correct_answer,
)
right_button.grid(row=1, column=1, padx=5, pady=5)

# calling the function to update the card before it enters the mainloop
wrong_answer()

window.mainloop()
