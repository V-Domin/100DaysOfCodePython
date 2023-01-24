import turtle
from turtle import Turtle, Screen
import random

jared = Turtle()
turtle.colormode(255)

def create_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# colors = ['green yellow', 'crimson', 'magenta', 'medium purple']

directions = [0, 90, 180, 270]
jared.width(15)
jared.speed("fastest")

for move in range(200):
    jared.color(create_color())
    jared.forward(30)
    jared.setheading(random.choice(directions))



screen = Screen()
screen.exitonclick()




