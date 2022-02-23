#! /usr/bin/env python3
# Password manager GUI project using tkinter

from tkinter import *
from tkinter import messagebox
import random, pyperclip

# file directories
LOGO_DIR = r"learning-programming\Python\21-50\37-password-manager-v1\logo.png"
DATA_DIR = r"learning-programming\Python\21-50\37-password-manager-v1"

FONT_NAME = "Times New Roman"
PASSWORD_LENGTH = 18
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# list of alphabets
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

# list of numbers
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# list of symbols
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def generate_password():
    """Generates a new password when generate password button is clicked"""
    number_of_letters = random.randint(8, 12)
    number_of_numbers = random.randint(2, 6)
    number_of_symbols = random.randint(2, 4)

    # list of randrom characters generated
    all_characters = (
        random.sample(letters, number_of_letters)
        + random.sample(numbers, number_of_numbers)
        + random.sample(symbols, number_of_symbols)
    )
    # shuffling the list
    random.shuffle(all_characters)

    # converting the list into a string
    password_generated = "".join(all_characters)

    # clearing the password entry box
    password_entry.delete(0, END)
    # inserting the new generated password i
    password_entry.insert(END, string=password_generated)

    # copying generated password to the clipboard
    pyperclip.copy(password_generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_entry():
    """Adds new entry into a txt file"""
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    # showing warning when the fields are empty
    if not website:
        messagebox.showwarning(title="Oops", message="Website field is empty.")
    elif not email:
        messagebox.showwarning(title="Oops", message="Email field is empty.")
    elif not password:
        messagebox.showwarning(title="Oops", message="Password field is empty.")

    else:
        # showing confirmation message
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered. \nEmail: {email}\nPassword: {password}\nIs it ok to save?",
        )
        # if user is ok with it, proceeds to write the data onto the txt file
        if is_ok:
            with open(
                f"{DATA_DIR}\\data.txt", "a"
            ) as data:  # "a": appends, "w": writes, "r": reads
                data.write(
                    website_entry.get()
                    + " | "
                    + email_username_entry.get()
                    + " | "
                    + password_entry.get()
                    + "\n"
                )
        # clearing the fields
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# setting up screen
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# setting up logo
canvas = Canvas(width=200, height=200)
try:
    logo_img = PhotoImage(file=LOGO_DIR)
except:
    print(f"Logo image not found in directory: {LOGO_DIR}")
# (100,100) is the position of logo. half of height and width of the canvas
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, padx=5, pady=5)

# website label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, padx=5, pady=5)

# email/username label
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0, padx=5, pady=5)

# password label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, padx=5, pady=5)

# Website entry
website_entry = Entry(width=53)
website_entry.focus()  # focus adds a cursor to the entry box
website_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

# Email/username entry
email_username_entry = Entry(width=53)
email_username_entry.insert(
    0, string="default_email@gmail.com"
)  # insert adds a default text in the entry box, index (0 or END) is where this text appears in the box
email_username_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

# Password entry
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, padx=5, pady=5)

# Add button
add_button = Button(text="Add", width=45, command=add_entry)
add_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

# Generate password button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, padx=5, pady=5, sticky="w")


# keeping the window on
window.mainloop()
