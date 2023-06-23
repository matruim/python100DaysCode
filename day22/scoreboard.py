import turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.playerScore = 0
        self.computerScore = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.computerScore, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.playerScore, align=ALIGNMENT, font=FONT)

    def update_computer_score(self):
        self.computerScore += 1
        self.write_score()

    def update_player_score(self):
        self.playerScore += 1
        self.write_score()

    def write_winning_message(self, winner):
        self.goto(0, 0)
        self.write(f"{winner} has won!!!", align=ALIGNMENT, font=("Courier", 24, "normal"))

    def check_winner(self):
        if self.playerScore >= 10:
            self.write_winning_message("Player on the Right")
            return True
        elif self.computerScore >= 10:
            self.write_winning_message("Player on the Left")
            return True
        else:
            return False
