import time
from turtle import Screen, done
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
sleep_time = 0.1
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    carManager.move_cars()

    if player.cross_finish_line():
        scoreboard.increase_level()
        carManager.new_level()
        player.new_level()
        sleep_time *= 0.9
        print(sleep_time)
        time.sleep(0.1)

    for car in carManager.cars:
        if abs(player.xcor() - car.xcor()) < 20 and abs(player.ycor() - car.ycor()) < 10:
            game_is_on = False
            scoreboard.game_over()
done()
