from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
count_min = None
count_sec = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="TIMER")
    canvas.itemconfig(timer_text, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_time)
        timer_label.config(text="LONG BREAK")
    elif reps % 2 == 0:
        count_down(short_break_time)
        timer_label.config(text="BREAK")

    else:
        count_down(work_time)
        timer_label.config(text="WORK TIME")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global count_min
    global count_sec
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    elif count == 0:

        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

pomodoro_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

timer_label = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 30, "bold"))


primary_button = Button(text="start", command=start_timer)
secondary_button = Button(text="reset", command=reset_timer)
check_mark= Label(text="", fg=GREEN, font=(FONT_NAME, 10,  "bold"))
timer_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
primary_button.grid(row=2, column=0)
secondary_button.grid(row=2, column=2)
check_mark.grid(row=2, column=1)











window.mainloop()
