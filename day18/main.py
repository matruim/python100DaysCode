import turtle


def draw_square(turtle: turtle.Turtle):
    for _ in range(0, 4):
        turtle.forward(100)
        turtle.right(90)


tim = turtle.Turtle()
tim.shape("turtle")
tim.color("red")
draw_square(tim)

screen = turtle.Screen()
screen.exitonclick()
