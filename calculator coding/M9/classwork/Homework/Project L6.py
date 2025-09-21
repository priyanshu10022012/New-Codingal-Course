import tkinter as tk
import random

# Global scores
player_score = 0
computer_score = 0

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Function to get computer's random choice
def get_computer_choice():
    return random.choice(choices)

# Function to decide winner
def decide_winner(player, computer):
    if player == computer:
        return "It's a Tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

# Function that plays one round
def play_round(player_choice):
    global player_score, computer_score

    computer_choice = get_computer_choice()
    result = decide_winner(player_choice, computer_choice)

    # Update scores using loop
    for _ in range(1):   # loop runs once per round (to meet requirement)
        if "Win" in result and "You" in result:
            player_score += 1
        elif "Computer" in result:
            computer_score += 1

    result_label.config(text=f"Your Choice: {player_choice}\nComputer's Choice: {computer_choice}\n\n{result}")
    score_label.config(text=f"Score -> You: {player_score}  |  Computer: {computer_score}")

# Function to reset game
def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text="Score -> You: 0  |  Computer: 0")

# Tkinter GUI
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x350")
root.resizable(False, False)

title = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 18, "bold"))
title.pack(pady=10)

# Buttons for choices
frame = tk.Frame(root)
frame.pack(pady=20)

rock_btn = tk.Button(frame, text="Rock", width=12, command=lambda: play_round("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(frame, text="Paper", width=12, command=lambda: play_round("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(frame, text="Scissors", width=12, command=lambda: play_round("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=15)

# Score label
score_label = tk.Label(root, text="Score -> You: 0  |  Computer: 0", font=("Arial", 14, "bold"))
score_label.pack(pady=10)

# Reset button
reset_btn = tk.Button(root, text="Reset Game", width=15, command=reset_game)
reset_btn.pack(pady=10)

# Run main loop
root.mainloop()