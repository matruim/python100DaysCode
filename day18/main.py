import turtle
import random
r = lambda: random.randint(0, 255)

def draw_square(ninja_turtle: turtle.Turtle):
    for _ in range(0, 4):
        ninja_turtle.forward(100)
        ninja_turtle.right(90)


def draw_dashed_line(ninja_turtle: turtle.Turtle):
    ninja_turtle.up()
    ninja_turtle.setpos(-200, 100)
    ninja_turtle.down()
    for _ in range(0,15):
        ninja_turtle.forward(10)
        ninja_turtle.penup()
        ninja_turtle.forward(10)
        ninja_turtle.pendown()


def draw_shapes(ninja_turtle: turtle.Turtle):
    ninja_turtle.up()
    ninja_turtle.up()
    ninja_turtle.setpos(200, -100)
    ninja_turtle.down()
    for i in range(3, 11):
        ninja_turtle.pencolor('#%02X%02X%02X' % (r(), r(), r()))
        for _ in range(i):
            ninja_turtle.fd(100)
            ninja_turtle.right(360/i)


tim = turtle.Turtle()
tim.shape("turtle")
tim.color("red")
draw_square(tim)
draw_dashed_line(tim)
draw_shapes(tim)

screen = turtle.Screen()

print(screen.screensize())
screen.exitonclick()
