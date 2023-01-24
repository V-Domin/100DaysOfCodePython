from tkinter import *
from math import floor

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
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(my_timer)
    canva.itemconfig(time, text="00:00")
    timer_text.config(text='Timer', fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_time_seconds = (WORK_MIN * 60)
    short_break_sec = (SHORT_BREAK_MIN * 60)
    long_break_sec = (LONG_BREAK_MIN * 60)

    # if it's 1, 3, 5, 7
    if reps % 2 != 0:
        count_down(work_time_seconds)
        timer_text.config(text="Work")
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_text.config(text="Long Chill", fg=RED)
    elif reps % 2 == 0 and reps != 8:
        count_down(short_break_sec)
        timer_text.config(text="Short Chill", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(number):
    global reps
    count_minutes = floor(number / 60)
    count_seconds = number % 60


    if count_seconds == 0:
        count_seconds = "00"
    elif count_seconds < 10:
        count_seconds = f'0{count_seconds}'

    canva.itemconfig(time, text=f"{count_minutes}:{count_seconds}")

    if number > 0:
        global my_timer
        my_timer = window.after(1000, count_down, number-1)
    else:
        start_timer()
        marks = ""
        work_sessions = floor(reps/2)
        for i in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro App')
window.config(padx=100, pady=50, background=YELLOW)


timer_text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, 'bold'))
timer_text.grid(column=1, row=0)

canva = Canvas(width=210, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canva.create_image(105, 112, image=tomato_img)
time = canva.create_text(103, 130, text="00:00", fill='white', font=(FONT_NAME, 27, 'bold'))
canva.grid(column=1, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 12), bd=1, activebackground=GREEN, highlightthickness=0,
                      command=start_timer)
start_button.grid(column=0, row=2)

start_reset = Button(text="Reset", font=(FONT_NAME, 12), bd=1, activebackground=RED, highlightthickness=0,
                     command=reset_timer)
start_reset.grid(column=2, row=2)

check_marks = Label(font=(20), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()