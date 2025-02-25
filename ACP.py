#Rock Paper Scissors
import tkinter as tk
from tkinter import messagebox
import random

def decide_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        return "You win!"
    else:
        return "You lose!"


def play(user_choice):
    comp_choice = random.choice(choices)
    result = decide_winner(user_choice, comp_choice)
    messagebox.showinfo("Result", f"You chose {user_choice}, computer chose {comp_choice}. {result}")


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x300")

choices = ["Rock", "Paper", "Scissors"]
label1=tk.Label(root, text="User Choice: Select any one")
label1.pack(pady=10)
rock_button = tk.Button(root, text="Rock", command=lambda: play("Rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda:  play("Paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play("Scissors"))
scissors_button.pack(pady=10)
root.mainloop()