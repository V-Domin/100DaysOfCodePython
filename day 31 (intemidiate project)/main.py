from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

try:
    data = pd.read_csv('words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv("german_words.csv")

to_learn = data.to_dict(orient="records")


def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(to_learn)
    canvas.itemconfig(german_word_image, image=card_front_img)
    canvas.itemconfig(word, text=random_word["German"], fill="black", font=(FONT_NAME, 60, 'bold'))
    canvas.itemconfig(title, text="German", fill="black", font=(FONT_NAME, 35, 'italic'))
    canvas.itemconfig(number_of_words, fill='black')
    flip_timer = window.after(3000, flip_card)


def next_card_right():
    to_learn.remove(random_word)
    words_to_learn = len(to_learn)
    next_card()
    to_learn_dictionary = pd.DataFrame(to_learn)
    to_learn_dictionary.to_csv("words_to_learn.csv", index=False)
    canvas.itemconfig(number_of_words, text=f"{words_to_learn} words to learn")

def flip_card():
    canvas.itemconfig(german_word_image, image=card_back_img)
    canvas.itemconfig(title, text="English", fill="white", font=(FONT_NAME, 35, 'italic'))
    canvas.itemconfig(word, text=random_word["English"], fill="white", font=(FONT_NAME, 60, 'bold'))
    canvas.itemconfig(number_of_words, fill="white")




window = Tk()
window.title("Flashy")
window.config(padx=50, pady=0, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=562, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
german_word_image = canvas.create_image(400, 281, image=card_front_img)
card_back_img = PhotoImage(file="images/card_back.png")

number_of_words = canvas.create_text(400, 65, font=(FONT_NAME, 12, 'italic'))
title = canvas.create_text(400, 150, text="German", font=(FONT_NAME, 35, 'italic'))
word = canvas.create_text(400, 263, text='Word', font=(FONT_NAME, 60, 'bold'))
canvas.grid(row=0, columnspan=2, column=0)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_image, highlightthickness=0, command=next_card_right)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()




window.mainloop()

