import turtle

HORIZONTAL_MULTIPLIER = 1
VERTICAL_MULTIPLIER = 5
SPEED = 20


class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.resizemode("user")
        self.shapesize(VERTICAL_MULTIPLIER, HORIZONTAL_MULTIPLIER)
        self.goto(position)
        self.color("white")

    def move(self, direction):
        new_y = self.ycor() + (SPEED * direction)
        if new_y >= 300 or new_y <= -300:
            pass
        else:
            self.goto(self.xcor(), new_y)
