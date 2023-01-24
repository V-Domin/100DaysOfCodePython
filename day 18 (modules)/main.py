import turtle
from turtle import Turtle, Screen
import random

jared = Turtle()
turtle.colormode(255)
jared.speed("fast")
jared.width(5)

def create_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_shape(num_sides):
    turn_right = 360 / num_sides
    for move in range(num_sides):
        jared.forward(100)
        jared.left(turn_right)


for move in range(3, 11):
    jared.color(create_color())
    draw_shape(move)


screen = Screen()
screen.exitonclick()

