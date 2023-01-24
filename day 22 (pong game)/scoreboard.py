from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 28, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.left_score = 0
        self.right_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.update_scores()

    def update_scores(self):
        self.goto(-100, 250)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    def count_left(self):
        self.left_score += 1
        self.clear()
        self.update_scores()

    def count_right(self):
        self.right_score += 1
        self.clear()
        self.update_scores()



