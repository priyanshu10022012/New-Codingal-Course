import tkinter as tk
import random

# Function to get computer choice
def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

# Function to decide winner
def decide_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

# Function called when user makes a choice
def play(user_choice):
    comp_choice = get_computer_choice()
    result = decide_winner(user_choice, comp_choice)
    result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {comp_choice}\n\n{result}")

# Tkinter window setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Buttons for user choices
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Run the GUI loop
root.mainloop()