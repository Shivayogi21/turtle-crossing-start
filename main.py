import time
from turtle import Screen

from car_manager import CarManager
from player import Player
# from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')  # Optional: Set background color
screen.title('Turtle Crossing Game')
screen.tracer(0)

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move_cars()

#   detect the collusion with the cars
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

#   detect the successful crossing
    if player.is_at_finishline():
        player.go_to_start()
        carmanager.level_up()
        scoreboard.increse_level()






screen.exitonclick()
