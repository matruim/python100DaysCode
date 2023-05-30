import turtle
import random

r = lambda: random.randint(0, 255)


def random_hex_color():
    return '#%02X%02X%02X' % (r(), r(), r())


def draw_square(ninja_turtle: turtle.Turtle):
    for _ in range(0, 4):
        ninja_turtle.forward(100)
        ninja_turtle.right(90)


def draw_dashed_line(ninja_turtle: turtle.Turtle):
    for _ in range(0, 15):
        ninja_turtle.forward(10)
        ninja_turtle.penup()
        ninja_turtle.forward(10)
        ninja_turtle.pendown()


def draw_shapes(ninja_turtle: turtle.Turtle):
    for i in range(3, 11):
        ninja_turtle.pencolor(random_hex_color())
        for _ in range(i):
            ninja_turtle.fd(100)
            ninja_turtle.right(360 / i)


def draw_random_walk(ninja_turtle: turtle.Turtle):
    ninja_turtle.pensize(15)
    ninja_turtle.speed(10)
    directions = [0, 90, 180, 270]
    for _ in range(0, 200):
        ninja_turtle.pencolor(random_hex_color())
        direction = random.choice(directions)
        ninja_turtle.setheading(direction)
        ninja_turtle.forward(30)
    ninja_turtle.speed(6)


tim = turtle.Turtle()
tim.shape("turtle")
tim.color(random_hex_color())
draw_square(tim)
tim.reset()
tim.color(random_hex_color())
draw_dashed_line(tim)
tim.reset()
draw_shapes(tim)
tim.reset()
draw_random_walk(tim)

screen = turtle.Screen()
screen.exitonclick()
