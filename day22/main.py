from turtle import Screen, done
import time
import paddle
import ball
import scoreboard


def setup_screen():
    canvas = Screen()
    canvas.setup(width=800, height=600)
    canvas.bgcolor("black")
    canvas.title("Pong")
    canvas.tracer(0)
    return canvas


def setup_listeners(window, padl, comp):
    window.listen()
    window.onkey(lambda: padl.move(1), "Up")
    window.onkey(lambda: padl.move(-1), "Down")
    window.onkey(lambda: comp.move(1), "w")
    window.onkey(lambda: comp.move(-1), "s")


def game_loop():
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with player paddle or the computer paddle
        if ball.distance(player) < 50 and ball.xcor() > 330 or ball.distance(computer) < 50 and ball.xcor() < -330:
            ball.bounce_x()

        if ball.xcor() > 380:
            scoreboard.update_computer_score()
            ball.reset()
            time.sleep(0.2)

        if ball.xcor() < -380:
            scoreboard.update_player_score()
            ball.reset()
            time.sleep(0.2)

        if scoreboard.check_winner():
            game_is_on = False


screen = setup_screen()
player = paddle.Paddle((350, 0))
computer = paddle.Paddle((-350, 0))
ball = ball.Ball()
scoreboard = scoreboard.Scoreboard()
setup_listeners(screen, player, computer)

game_loop()
done()
