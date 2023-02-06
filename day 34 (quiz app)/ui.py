from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface():

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.window.geometry("350x600")

        self.score_label = Label(text=f"Score:0", font=('Arial', 12), background=THEME_COLOR, pady=20, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Here goes one of the questions...",
                                                     font=('Arial', 15, 'italic'), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=35)

        right_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")

        self.right_button = Button(image=right_img, highlightthickness=0, command=self.choose_true)
        self.right_button.grid(column=0, row=2)
        self.false_button = Button(image=wrong_img, highlightthickness=0, command=self.choose_false)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas['background'] = "white"
        else:
            self.canvas['background'] = "white"
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of the Quiz! Your final score: {self.quiz.score}/10")
            self.false_button.config(state='disabled')
            self.right_button.config(state='disabled')
            self.score_label.config(text="")


    def choose_true(self):
        self.is_right = self.quiz.check_answer("True")
        self.give_feedback(self.is_right)

    def choose_false(self):
        self.is_right = self.quiz.check_answer("False")
        self.give_feedback(self.is_right)

    def change_bg(self):
        if self.is_right == True:
            self.canvas['background'] = "green"
        else:
            self.canvas['background'] = "red"

    def give_feedback(self, is_right):
        self.window.after(1000, func=self.change_bg)
        self.window.after(3000, func=self.get_next_question)

