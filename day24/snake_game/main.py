import turtle
import time
import snake
from day24.snake_game import food
import scoreboard


def setup_listenter(window, player):
    window.listen()
    window.onkey(player.up, "Up")
    window.onkey(player.down, "Down")
    window.onkey(player.left, "Left")
    window.onkey(player.right, "Right")


def setup_screen():
    canvas = turtle.Screen()
    canvas.setup(width=600, height=600)
    canvas.bgcolor("black")
    canvas.title("Snake")
    canvas.tracer(0)
    return canvas


def game_running(player, canvas):
    game_is_on = True
    while game_is_on:
        canvas.update()
        time.sleep(0.1)
        player.move()

        # Detect collision with food
        if player.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()
            player.extend()

        # Detect Collision with Wall
        if player.head.xcor() >= 300 or player.head.xcor() <= -300 or player.head.ycor() >= 300 or player.head.ycor() <= -300:
            scoreboard.reset()
            player.reset()

        # Detect Collision with Tail
        for segment in player.segments[1:]:
            if player.head.distance(segment) < 10:
                scoreboard.reset()
                player.reset()


screen = setup_screen()
snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()
setup_listenter(screen, snake)
screen.update()
game_running(snake, screen)

turtle.done()
