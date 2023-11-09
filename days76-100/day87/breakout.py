import tkinter as tk

class Breakout:
    def __init__(self, master):
        self.master = master
        self.master.title("Breakout Game")
        self.master.geometry("600x600")
        self.master.resizable(False, False)

        self.canvas = tk.Canvas(self.master, bg="black", width=600, height=600)
        self.canvas.pack()

        self.paddle = self.canvas.create_rectangle(250, 550, 350, 570, fill="white")
        self.ball = self.canvas.create_oval(300, 300, 320, 320, fill="white")

        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]

        self.bricks = []
        for row in range(6):
            color = self.colors[row % len(self.colors)]  # Choose color for the row
            for col in range(10):
                x = 50 + col * 50
                y = 50 + row * 20
                brick = self.canvas.create_rectangle(x, y, x + 40, y + 15, fill=color)
                self.bricks.append(brick)

        self.master.bind("<Left>", self.move_paddle_left)
        self.master.bind("<Right>", self.move_paddle_right)

        self.dx = 3
        self.dy = -3

        self.master.after(10, self.move_ball)

    def move_paddle_left(self, event):
        current_x = self.canvas.coords(self.paddle)[0]
        if current_x > 0:
            self.canvas.move(self.paddle, -20, 0)

    def move_paddle_right(self, event):
        current_x = self.canvas.coords(self.paddle)[2]
        if current_x < 600:
            self.canvas.move(self.paddle, 20, 0)

    def move_ball(self):
        self.canvas.move(self.ball, self.dx, self.dy)

        ball_pos = self.canvas.coords(self.ball)

        if ball_pos[1] <= 0 or ball_pos[3] >= 600:
            self.dy *= -1

        if ball_pos[0] <= 0 or ball_pos[2] >= 600:
            self.dx *= -1

        if ball_pos[3] >= 600:  # Check if the ball hits the bottom
            self.game_over()

        if self.collides_with_paddle():
            self.dy *= -1

        self.check_collision_with_bricks()

        self.master.after(10, self.move_ball)

    def collides_with_paddle(self):
        paddle_pos = self.canvas.coords(self.paddle)
        ball_pos = self.canvas.coords(self.ball)

        return paddle_pos[0] < ball_pos[2] and paddle_pos[2] > ball_pos[0] and paddle_pos[1] < ball_pos[3] and paddle_pos[3] > ball_pos[1]

    def check_collision_with_bricks(self):
        ball_pos = self.canvas.coords(self.ball)

        for brick in self.bricks.copy():  # Copy to avoid modifying the list during iteration
            brick_pos = self.canvas.coords(brick)
            if brick_pos[0] < ball_pos[2] and brick_pos[2] > ball_pos[0] and brick_pos[1] < ball_pos[3] and brick_pos[3] > ball_pos[1]:
                self.canvas.delete(brick)
                self.bricks.remove(brick)
                self.dy *= -1

        if not self.bricks:  # Check if all bricks are destroyed
            self.game_over(win=True)


    def game_over(self, win=False):
        if win:
            self.canvas.create_text(300, 300, text="You Won!", font=("Helvetica", 16), fill="red")
        else:
            self.canvas.create_text(300, 300, text="Game Over", font=("Helvetica", 16), fill="red")
        self.master.after(2000, self.master.destroy)  # Close the window after 2 seconds


if __name__ == "__main__":
    root = tk.Tk()
    game = Breakout(root)
    root.mainloop()
