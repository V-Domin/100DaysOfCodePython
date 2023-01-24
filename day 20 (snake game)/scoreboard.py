from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 14, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        with open('data.txt', 'r') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.high_score}", align='center',  font=('Arial', 14, 'normal'))


    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()



    def count_score(self):
        self.score += 1
        self.update_score()



    # def end_game(self):
    #     self.setposition(0, 0)
    #     self.write("GAME OVER.", align=ALIGNMENT, font=FONT)

