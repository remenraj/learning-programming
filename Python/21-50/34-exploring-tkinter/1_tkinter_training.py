from tkinter import *


def button_clicked():
    """ This function is called when the button is clicked. Changes the label text. """
    # my_label.config(text="Button is clicked")
    my_label.config(text=input.get())


# creating the screen
window = Tk()
# setting the title
window.title("Hello World")
# setting the size
window.minsize(width=500, height=500)
# add padding
# window.config(padx=100, pady=200)


# Label
my_label = Label(text="Hello World", font=("Arial", 20, "bold"))
# my_label["text"] = "New Text"
# my_label.config(text= "New Text")
my_label.grid(column=0, row=0)


# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# New Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=0)

# Text box Entry
input = Entry(width="10")
input_text = input.get()
input.grid(column=3, row=3)

# keeping the window on the screen
window.mainloop()
