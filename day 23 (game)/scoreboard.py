from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(-250, 250)
        self.level = 1
        self.write(f"Level: {self.level}", font=FONT)


    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)


    def next_level(self):
        self.level += 1
        self.update_level()


    def end_game(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)
