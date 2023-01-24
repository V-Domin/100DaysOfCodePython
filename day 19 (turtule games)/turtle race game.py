from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(500, 400)
is_race_on = False
user_bet = screen.textinput("Make a bet!", "Who do you think will win? Enter a color: ")
colors = ['green', 'red', 'yellow', 'orange', 'purple', 'blue']
all_turtles = []

y_line = -170

for turtle in range(0, 6):
    y_line += 50
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(-240, y_line)
    color = colors[turtle]
    new_turtle.color(color)
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >= 210:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! Congrats! Winning color is: {winning_color}")
            else:
                print(f"You were wrong! Winning color is: {winning_color}")


            is_race_on = False


        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()