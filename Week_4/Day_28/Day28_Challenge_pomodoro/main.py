import math
import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
SEC_PER_MIN = 60
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, marks
    if timer is not None:
        window.after_cancel(str(timer))
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    marks = ""
    check_marks.config(text=marks)
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, marks
    reps += 1
    work_sec = WORK_MIN * SEC_PER_MIN
    short_break_sec = SHORT_BREAK_MIN * SEC_PER_MIN
    long_break_sec = LONG_BREAK_MIN * SEC_PER_MIN

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        check_marks.config(text=marks)
        count_down(work_sec)
        if (reps + 2) % 4 == 1:
            marks += "✔"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Text
title_label = tk.Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN, justify="center")
title_label.grid(column=1, row=0)

check_marks = tk.Label(font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN, justify="center")
check_marks.grid(column=1, row=3)

# Button
start_button = tk.Button(text="Start", font=(FONT_NAME, 10, "bold"),
                         justify="right", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", font=(FONT_NAME, 10, "bold"),
                         justify="right", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
