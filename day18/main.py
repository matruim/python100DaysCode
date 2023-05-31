import turtle
import random
import colorgram
import os

absolute_path = os.path.dirname(__file__)


def random_hex_color():
    return '#' + ''.join(random.choices('0123456789ABCDEF', k=6))


def random_rgb_color():
    turtle.colormode(255)
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def draw_square(ninja_turtle):
    ninja_turtle.pensize(1)
    for _ in range(4):
        ninja_turtle.pencolor(random_rgb_color())
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


def draw_random_spirograph(ninja_turtle, size_of_gap):
    ninja_turtle.speed(0)
    radius = 100
    for _ in range(int(360 / size_of_gap)):
        ninja_turtle.pencolor(random_hex_color())
        ninja_turtle.circle(radius)
        ninja_turtle.setheading(ninja_turtle.heading() + size_of_gap)


def draw_random_dots(ninja_turtle, image):
    colors = colorgram.extract(os.path.join(absolute_path, image), 30)
    ninja_turtle.hideturtle()
    print(random.choice(colors).rgb)
    ninja_turtle.speed(0)
    ninja_turtle.penup()
    ninja_turtle.setpos(-(turtle.window_width()/2 - 35), -(turtle.window_height()/2 - 35))
    for _ in range(int(turtle.window_height() / 100) + 1):
        for _ in range(int(turtle.window_width() / 100)):
            ninja_turtle.dot(50, (random.choice(colors)).rgb)
            ninja_turtle.forward(100)
        ninja_turtle.setx(-(turtle.window_width()/2 - 35))
        ninja_turtle.sety(ninja_turtle.ycor() + 100)
    ninja_turtle.showturtle()


turtle.colormode(255)
tim = turtle.Turtle()
tim.shape('turtle')

draw_square(tim)
tim.reset()

draw_dashed_line(tim)
tim.reset()

draw_shapes(tim)
tim.reset()

draw_random_walk(tim)
tim.reset()

draw_random_spirograph(tim, 5)
tim.reset()

draw_random_dots(tim, 'images.jpeg')

turtle.Screen().exitonclick()
