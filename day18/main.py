import turtle
import random


def random_hex_color():
    return '#' + ''.join(random.choices('0123456789ABCDEF', k=6))


def draw_square(ninja_turtle):
    ninja_turtle.pensize(1)
    for _ in range(4):
        ninja_turtle.forward(100)
        ninja_turtle.right(90)


def draw_dashed_line(ninja_turtle):
    ninja_turtle.pensize(1)
    for _ in range(15):
        ninja_turtle.forward(10)
        ninja_turtle.penup()
        ninja_turtle.forward(10)
        ninja_turtle.pendown()


def draw_shapes(ninja_turtle):
    ninja_turtle.pensize(1)
    for i in range(3, 11):
        ninja_turtle.pencolor(random_hex_color())
        for _ in range(i):
            ninja_turtle.fd(100)
            ninja_turtle.right(360 / i)


def draw_random_walk(ninja_turtle):
    ninja_turtle.pensize(15)
    ninja_turtle.speed(10)
    directions = [0, 90, 180, 270]
    for _ in range(200):
        ninja_turtle.pencolor(random_hex_color())
        direction = random.choice(directions)
        ninja_turtle.setheading(direction)
        ninja_turtle.forward(30)
    ninja_turtle.speed(6)


tim = turtle.Turtle()
tim.shape('turtle')

draw_square(tim)
tim.reset()

draw_dashed_line(tim)
tim.reset()

draw_shapes(tim)
tim.reset()

draw_random_walk(tim)

turtle.Screen().exitonclick()
