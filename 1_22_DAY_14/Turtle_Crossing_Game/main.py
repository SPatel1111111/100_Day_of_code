from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from player import Player
from car_manager import CarManager
import time

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_m = CarManager()
scoreboard = ScoreBoard()
screen.listen()
screen.onkeypress(player.go_up, "Up")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_m.create_cars()
    car_m.move_cars()
    scoreboard.update_score()

    # collision with cars
    for car in car_m.car_list:
        if car.distance(player) < 20:
            is_game_on = False
            scoreboard.game_over()

    # reach to the finishing line
    if player.is_finishing_line():
        player.goto_starting()
        car_m.level_up()
        scoreboard.increase_score()

screen.exitonclick()
