############ Pomodoro App ############

# Pomodoro technique
# ------------------------#
# 1. Work for 25 minutes
# 2. Take a break of 5 minutes
# 3. Work for 25 minutes
# 4. Take a break of 5 minutes
# 5. Work for 25 minutes
# 6. Take a break of 5 minutes
# 7. Work for 25 minutes
# 8. Take a long break of 20 minutes

from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
# colors taken from: https://colorhunt.co/
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 1
timer = None

# tomato image file directory
TOMATO_FILE_DIR = r"C:\Users\Cylon\OneDrive\Programming\git\Workspace\100-days-of-code\day-28-pomodoro-app\tomato.png"

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")

    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    start_button.grid_forget()
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        reps = 0
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)

    elif reps % 2 == 0:
        reps += 1
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)

    else:
        reps += 1
        count_down(work_sec)
        timer_label.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checkmarks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            checkmarks += "✔"
        checkmark_label.config(text=checkmarks)


# ---------------------------- UI SETUP ------------------------------- #
# setting up screen
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# setting up tomato as background image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=TOMATO_FILE_DIR)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1)

# timer label
timer_label = Label(
    text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50), highlightthickness=0
)
timer_label.grid(row=0, column=1)


# start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)


# reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# checkmark label
checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20), highlightthickness=0)
checkmark_label.grid(row=3, column=1)

window.mainloop()
