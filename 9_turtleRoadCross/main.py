import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.go_up,key="Up")
game_is_on = True
car =  CarManager()
score_board = Scoreboard()

while game_is_on:
    time.sleep(.1)
    screen.update()

    car.create_car()
    car.move_car()

    for cars in car.all_cars:
        if cars.distance(player) <20 :
            game_is_on = False
            score_board.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        player.level_up()
        score_board.level_increase()
screen.exitonclick()