import turtle


def draw_square(ninja_turtle: turtle.Turtle):
    for _ in range(0, 4):
        ninja_turtle.forward(100)
        ninja_turtle.right(90)


tim = turtle.Turtle()
tim.shape("turtle")
tim.color("red")
draw_square(tim)

screen = turtle.Screen()
screen.exitonclick()
