#! /usr/bin/env python3
# Program to display a random quote by Kanye using Kanye api

from tkinter import *
import requests

# file directories
try:
    BACKGROUND_DIR = r"learning-programming\Python\21-50\43-kanye-quotes\background.png"
    KANYE_IMG_DIR = r"learning-programming\Python\21-50\43-kanye-quotes\kanye.png"
except FileNotFoundError:
    print("File not found")


def get_quote():
    """Get a random quote from Kanye's API"""
    # get quote from kanye api
    response = requests.get("https://api.kanye.rest/")
    # raise exception if response is not 200
    response.raise_for_status()
    quote = response.json()["quote"]
    # printing the quote on the screen
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=BACKGROUND_DIR)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150, 207, text="Kanye Quotes", width=250, font=("Arial", 20, "bold"), fill="white"
)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=KANYE_IMG_DIR)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
