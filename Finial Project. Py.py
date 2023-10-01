#
#Program: Rock paper Scissors
#Programer: Maricela Manuel




import tkinter as tk
from tkinter import messagebox
from random import choice

# Function to play the game and determine the winner
def play_game(player_choice):
    computer_choice = choice(["Rock", "Paper", "Scissors"])
    result_label.config(text=f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Scissors" and computer_choice == "Paper")
        or (player_choice == "Paper" and computer_choice == "Rock")
    ):
        result_label.config(text="You win!")
    else:
        result_label.config(text="Computer wins!")

# Function to exit the application
def exit_game():
    root.quit()

# Function to validate user input
def validate_input():
    player_choice = entry.get()
    if player_choice not in ["Rock", "Paper", "Scissors"]:
        messagebox.showerror("Invalid Input", "Please enter Rock, Paper, or Scissors.")
    elif not player_choice:
        messagebox.showerror("Empty Input", "Please enter your choice.")
    else:
        play_game(player_choice)

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Create and place labels
instruction_label = tk.Label(root, text="Enter your choice (Rock, Paper, or Scissors):")
instruction_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Create and place entry widget
entry = tk.Entry(root)
entry.pack()

# Create and place buttons with background colors
play_button = tk.Button(root, text="Play", command=validate_input, bg="green", fg="white")
play_button.pack()

exit_button = tk.Button(root, text="Exit", command=exit_game, bg="red", fg="white")
exit_button.pack()

# Run the main loop
root.mainloop()
