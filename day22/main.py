from turtle import Turtle, Screen, done
import time
import paddle
import ball
import scoreboard


# create window to display the game
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
        ball.move(ball.heading())

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


screen = setup_screen()

# create the paddles for the players or the player and computer
player = paddle.Paddle((350, 0))
computer = paddle.Paddle((-350, 0))

# create the ball
ball = ball.Ball()

# create the scoreboard and set the score to 0 for both players
scoreboard = scoreboard.Scoreboard()

# handle game over events

setup_listeners(screen, player, computer)
game_loop()

done()
