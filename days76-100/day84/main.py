# Tic tac toe game created by chat GPT
import tkinter as tk

root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons for the game grid
buttons = [[None, None, None], [None, None, None], [None, None, None]]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", height=2, width=5, command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

# Initialize global variables
global game_over
game_over = False
global current_player
current_player = "X"
global player_x_score
player_x_score = 0
global player_o_score
player_o_score = 0

def button_click(row, col):
    global game_over, current_player
    if buttons[row][col]["text"] == "" and not game_over:
        buttons[row][col]["text"] = current_player
        check_win()
        if game_over:
            show_win_message(current_player)
            update_scores(current_player)
        elif all(buttons[i][j]["text"] for i in range(3) for j in range(3)):
            show_draw_message()
            game_over = True
        switch_player()

def check_win():
    global game_over
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            mark_winner(i, 0, i, 1, i, 2)
            game_over = True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            mark_winner(0, i, 1, i, 2, i)
            game_over = True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        mark_winner(0, 0, 1, 1, 2, 2)
        game_over = True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        mark_winner(0, 2, 1, 1, 2, 0)
        game_over = True

def mark_winner(x1, y1, x2, y2, x3, y3):
    for (x, y) in [(x1, y1), (x2, y2), (x3, y3)]:
        buttons[x][y].config(bg="green")

def show_win_message(player):
    global player_x_score, player_o_score
    label.config(text=f"Player {player} Wins!", bg="green")
    if player == "X":
        player_x_score += 1
        player_x_label.config(text=f"Player X: {player_x_score}")
    else:
        player_o_score += 1
        player_o_label.config(text=f"Player O: {player_o_score}")

def show_draw_message():
    label.config(text="It's a Draw!", bg="gray")

def update_scores(player):
    global player_x_score, player_o_score
    if player == "X":
        player_x_score += 1
        player_x_label.config(text=f"Player X: {player_x_score}")
    else:
        player_o_score += 1
        player_o_label.config(text=f"Player O: {player_o_score}")

def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"

def restart_game():
    global game_over, current_player
    game_over = False
    current_player = "X"
    label.config(text="Tic-Tac-Toe", bg="white")
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal", bg="white")

def exit_game():
    root.destroy()

restart_button = tk.Button(root, text="Restart", command=restart_game)
exit_button = tk.Button(root, text="Exit", command=exit_game)

restart_button.grid(row=3, column=0)
exit_button.grid(row=3, column=2)

player_x_label = tk.Label(root, text=f"Player X: {player_x_score}", font=("Helvetica", 12))
player_x_label.grid(row=4, column=0)

label = tk.Label(root, text="Tic-Tac-Toe", font=("Helvetica", 16))
label.grid(row=4, column=1)

player_o_label = tk.Label(root, text=f"Player O: {player_o_score}", font=("Helvetica", 12))
player_o_label.grid(row=4, column=2)

root.mainloop()
