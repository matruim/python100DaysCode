from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.seth(90)
        self.new_level()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def cross_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def new_level(self):
        self.goto(STARTING_POSITION)
