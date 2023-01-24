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

jared.speed("fastest")


def draw_spirograph(space_between):
    for i in range(int(360 / space_between)):
        jared.color(create_color())
        jared.circle(100)
        jared.setheading(jared.heading() + space_between)


draw_spirograph(4)







screen = Screen()
screen.exitonclick()