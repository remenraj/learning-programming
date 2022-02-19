# mile to kilometer converter GUI project using tkinter module

from tkinter import *

# font size
FONT_SIZE = 12


def miles_to_km():
    """ Converts miles to kilometers """
    # my_label.config(text="Button is clicked")
    miles_entered = float(miles_input.get())
    km_converted = round(miles_entered * 1.609, 2)
    converted_value_label.config(text=f"{km_converted}")
    pass


# creating the screen
window = Tk()
# setting the title
window.title("Mile to Km Converter")
# setting the size
# window.minsize(width=200, height=100)
# add padding
window.config(padx=50, pady=20)

# Entry
miles_input = Entry(width="8")
# insert adds a default text in the entry box
miles_input.insert(END, string="1")
# focus adds a cursor in entry box
miles_input.focus()
miles_input.grid(column=1, row=0)


# label miles
miles_label = Label(text="Miles", font=("Arial", FONT_SIZE, "normal"))
miles_label.grid(column=2, row=0)

# label is_equal_to
is_equal_to_label = Label(text="is equal to", font=("Arial", FONT_SIZE, "normal"))
is_equal_to_label.grid(column=0, row=1)

# label converted_value
converted_value_label = Label(text="1.61", font=("Arial", FONT_SIZE, "bold"))
converted_value_label.grid(column=1, row=1)

# label Km
km_label = Label(text="Km", font=("Arial", FONT_SIZE, "normal"))
km_label.grid(column=2, row=1)

# button calculate
button_calculate = Button(text="Calculate", command=miles_to_km)
button_calculate.grid(column=1, row=2)


# keeping the window on the screen
window.mainloop()
