import turtle

tim = turtle.Turtle()
screen = turtle.Screen()


def move_forwards():
    tim.fd(10)


def move_backwards():
    tim.bk(10)


def move_counter_clockwise():
    tim.left(10)


def move_clockwise():
    tim.right(10)


def clear():
    screen.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
