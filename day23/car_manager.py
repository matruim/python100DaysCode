from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_WIDTH = 40


class CarManager:
    def __init__(self):
        self.cars = []
        for _ in range(0, 20):
            self.create_cars()

        self.new_level()

    def create_cars(self):
        new_car = Turtle("square")
        new_car.turtlesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.seth(180)
        new_car.forward(STARTING_MOVE_DISTANCE)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.goto(320, car.ycor())
            car.forward(MOVE_INCREMENT)

    def new_level(self):
        for car in self.cars:
            while True:
                x = random.randrange(-200, 325)
                y = random.randrange(-250, 250)
                # Check if new car position is too close to any existing car
                if not self.is_car_too_close(x, y):
                    car.goto(x, y)
                    break

    def is_car_too_close(self, x, y):
        for car in self.cars:
            if abs(car.xcor() - x) < CAR_WIDTH and abs(car.ycor() - y) < CAR_WIDTH:
                return True
        return False
