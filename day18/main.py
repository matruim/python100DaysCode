from turtle import Turtle, Screen


def draw_square(turtle: Turtle):
    for _ in range(0, 4):
        turtle.forward(100)
        turtle.right(90)


tim = Turtle()
tim.shape("turtle")
tim.color("red")
draw_square(tim)

screen = Screen()
screen.exitonclick()
