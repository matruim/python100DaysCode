import turtle


def draw_square(ninja_turtle: turtle.Turtle):
    for _ in range(0, 4):
        ninja_turtle.forward(100)
        ninja_turtle.right(90)


def draw_dashed_line(ninja_turtle: turtle.Turtle):
    ninja_turtle.up()
    ninja_turtle.setpos(-500, 300)
    ninja_turtle.down()
    for _ in range(0,15):
        ninja_turtle.forward(10)
        ninja_turtle.penup()
        ninja_turtle.forward(10)
        ninja_turtle.pendown()

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("red")
draw_square(tim)
draw_dashed_line(tim)

screen = turtle.Screen()
screen.exitonclick()
