import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('Pong Game')

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')

screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # Detect collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when the ball goes out of the right borders
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.count_left()

    # Detect when the ball goes out of the left borders
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.count_right()


screen.exitonclick()