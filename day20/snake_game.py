import turtle
import time
import snake


def setup_listenter(screen, snake):
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


def setup_screen():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)
    return screen


def game_running(snake, canvas):
    game_is_on = True
    while game_is_on:
        canvas.update()
        time.sleep(0.1)
        snake.move()


screen = setup_screen()
snake = snake.Snake()
setup_listenter(screen, snake)
screen.update()
game_running(snake, screen)

turtle.done()
