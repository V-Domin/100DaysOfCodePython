from turtle import Turtle, Screen
import random
screen = Screen()
jared = Turtle()
screen.colormode(255)

def get_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r, g, b)
    return rgb_color

width = jared.width(1)

def move_forward():
    jared.forward(10)
def move_back():
    jared.back(10)
def turn_left():
    jared.left(10)
def turn_right():
    jared.right(10)

def clear_screen():
    screen.reset()

def add_width():
    jared.width(5)

def minus_width():
    jared.width(1)

def pen_up():
    jared.penup()

def pen_down():
    jared.pendown()

def change_color():
    jared.color(get_color())


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="q", fun=add_width)
screen.onkey(key="e", fun=minus_width)
screen.onkey(key="z", fun=pen_up)
screen.onkey(key="x", fun=pen_down)

screen.onkey(key="k", fun=change_color)




screen.exitonclick()