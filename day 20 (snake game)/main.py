from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.tracer(0)
screen.title("Snake Game")


snake = Snake()
food = Food()
board = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True



while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        board.clear()
        board.count_score()

    # Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -280:
        board.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            board.reset()
            snake.reset()








screen.exitonclick()