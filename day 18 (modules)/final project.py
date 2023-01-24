import colorgram
from turtle import Screen, Turtle
import random

# colors = colorgram.extract('painting.jpg', 15)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     nex_colors = (r, g, b)
#     rgb_colors.append(nex_colors)
# print(rgb_colors)

screen = Screen()
jared = Turtle()
screen.colormode(255)

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
              (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
              (64, 153, 138), (39, 36, 36), (76, 40, 48)]


# def create_color():
#     rgb_color = random.choice(color_list)
#     r = rgb_color[0]
#     g = rgb_color[1]
#     b = rgb_color[2]
#     color = (r, g, b)
#     return color


jared.speed('fastest')
jared.penup()


jared.back(250)
jared.right(90)
jared.forward(200)
jared.setheading(0)

def draw_line():
    for move in range(10):
        jared.penup()
        jared.color(random.choice(color_list))
        jared.dot(20)
        jared.forward(50)


for move in range(10):
    draw_line()
    jared.goto(-250, jared.ycor() + 30)


jared.hideturtle()




screen.exitonclick()
