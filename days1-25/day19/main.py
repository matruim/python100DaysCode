import turtle
import random


def setup_screen():
    screen = turtle.Screen()
    screen.setup(width=500, height=400)
    screen.title("Turtle Racer")
    return screen


def get_user_bet(screen):
    return screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


def create_turtles(colors):
    turtles = []
    for i, color in enumerate(colors):
        t = turtle.Turtle("turtle")
        t.color(color)
        t.penup()
        t.goto(x=-230, y=(-70 + 30 * i))
        turtles.append(t)
    return turtles


def check_win_condition(t, colors, bet_index):
    if t.xcor() >= 220:
        t.goto(0,30)
        t.pencolor("black")  # Set text color to black for better visibility
        if t.color()[0] == colors[bet_index]:
            t.write("WINNER", align="center", font=("Arial", 25, 'normal'))
        else:
            t.write("Better Luck Next Time", align="center", font=("Arial", 25, 'normal'))
        t.home()
        animate_spin(t)
        return True
    return False


def animate_spin(t):
    for _ in range(12):  # Rotate the turtle 12 times
        t.right(30)
        turtle.delay(100)  # Add a small delay for smoother animation


def race(turtles, colors, user_bet):
    is_race_on = bool(user_bet)
    bet_index = colors.index(user_bet) if user_bet else None

    while is_race_on:
        for t in turtles:
            t.forward(random.randint(0, 10))
            if check_win_condition(t, colors, bet_index):
                is_race_on = False
                break


def main():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    screen = setup_screen()
    user_bet = get_user_bet(screen)
    turtles = create_turtles(colors)
    race(turtles, colors, user_bet)
    turtle.done()


if __name__ == "__main__":
    main()
