#! /usr/bin/env python3
# Password Manager GUI Project v2

from tkinter import *
from tkinter import messagebox
import random, pyperclip, json
from characters import letters, symbols, numbers


# file directories
try:
    LOGO_DIR = r"Workspace\100-days-of-code\day-29-30-password-manager\v2\logo.png"
    DATA_DIR = r"Workspace\100-days-of-code\day-29-30-password-manager\v2"
except FileNotFoundError:
    print("File not found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


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
    # inserting the new generated password
    password_entry.insert(END, string=password_generated)

    # copying generated password to the clipboard
    pyperclip.copy(password_generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_entry():
    """Adds new entry into a json file"""
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    # creating new entry dictionary
    new_entry = {website: {"email": email, "password": password}}
    # checking if the fields are empty
    if not website:
        messagebox.showwarning(title="Oops", message="Website field is empty.")
    elif not email:
        messagebox.showwarning(title="Oops", message="Email field is empty.")
    elif not password:
        messagebox.showwarning(title="Oops", message="Password field is empty.")

    else:
        # asking the user if he/she wants to save the password
        # is_ok = messagebox.askokcancel(
        #     title=website,
        #     message=f"These are the details entered. \nEmail: {email}\nPassword: {password}\nIs it ok to save?",
        # )
        # saving the data if the user clicks ok
        # if is_ok:

        # opening the json file
        try:
            with open(f"{DATA_DIR}\\data_file.json", "r") as data_file:
                # reading old data
                try:
                    data = json.load(data_file)
                except json.decoder.JSONDecodeError:
                    data = {}
                # updating old data with new data
                data.update(new_entry)

        except FileNotFoundError:  # except block runs if try block raises an exception
            with open(f"{DATA_DIR}\\data_file.json", "w") as data_file:
                json.dump(
                    new_entry, data_file, indent=4
                )  # indent is used to make the json file more readable

        else:  # else runs if the try block doesn't raise any error
            # writing the new data to the file
            with open(f"{DATA_DIR}\\data_file.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:  # finally runs even if there is an error
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH ENTRY ------------------------------- #


def search_entry():
    """Displays the email and password of the website entered"""
    website = website_entry.get()
    # checking if the fields are empty
    if not website:
        messagebox.showwarning(title="Oops", message="Website field is empty.")
    else:
        # opening the json file
        try:
            with open(f"{DATA_DIR}\\data_file.json", "r") as data_file:
                # reading old data
                try:
                    data = json.load(data_file)
                except json.decoder.JSONDecodeError:
                    print("No data found in the file")
                else:
                    if website in data:
                        messagebox.showinfo(
                            title=website,
                            message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}",
                        )
                    else:
                        messagebox.showinfo(
                            title=website, message=f"{website} not found"
                        )

        except FileNotFoundError:  # except block runs if try block raises an exception
            messagebox.showwarning(title="Oops", message="No data file found")


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
website_entry = Entry(width=33)
website_entry.focus()  # focus adds a cursor to the entry box
website_entry.grid(row=1, column=1, padx=5, pady=5)

# Email/username entry
email_username_entry = Entry(width=53)
email_username_entry.insert(
    0, string="default_mail@gmail.com"
)  # insert adds a default text in the entry box, index (0/END) is where this text appears in the box
email_username_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

# Password entry
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, padx=5, pady=5)

# Add button
add_button = Button(text="Add", width=45, command=add_entry)
add_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

# Generate password button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, padx=5, pady=5)

# search button
search_button = Button(text="Search", width=14, command=search_entry)
search_button.grid(row=1, column=2, padx=5, pady=5)

# keeping the window on
window.mainloop()
