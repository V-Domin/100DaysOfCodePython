from turtle import Turtle

STARTING_POSITION = (0, -250)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)
