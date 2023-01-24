import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.up, 'Up')
car_manager = CarManager()



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with a car => Game over
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            score_board.end_game()
            game_is_on = False

    # Detect crossing the road successfully => The next level
    if player.ycor() > 250:
        score_board.next_level()
        player.goto(0, -250)
        car_manager.move_cars_faster()






screen.exitonclick()