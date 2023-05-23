import tkinter as tk
from tkinter import messagebox
import random

# List of available colors
colors = ['red', 'yellow', 'orange', 'green', 'blue']

# Initialize scores
computer_score = 0
player_score = 0

# Function to check the result and update scores
def check_result():
    global computer_score, player_score
    
    # Get the player's choice from the dropdown menu
    player_choice = color_var.get()
    
    # Generate a random choice for the computer
    computer_choice = random.choice(colors)
    
    # Compare choices and update scores
    if player_choice == computer_choice:
        player_score += 1
        result_label.config(text="Correct! You scored a point.")
    else:
        computer_score += 1
        result_label.config(text="Wrong! Computer scored a point.")
    
    # Update scores on the labels
    player_score_label.config(text=f"Player Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    
    # Show a message box with the computer's choice
    messagebox.showinfo("Computer's Choice", f"The computer chose: {computer_choice}")

# Create the main window
window = tk.Tk()
window.title('Color Choices Game')

# Set the window size and position it in the center of the screen
window_width = 400
window_height = 250
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a label for the game instructions
instructions_label = tk.Label(window, text="Winning Rules of the Color Choices Game:\n\n"
                                           "Enter a number from 1 to 5 and match the computer's choice to win.",
                             font=("Arial", 12), wraplength=350)
instructions_label.pack(pady=10)

# Create a label for the player's choice
player_label = tk.Label(window, text="Select a color:", font=("Arial", 14))
player_label.pack()

# Create a dropdown menu for color selection
color_var = tk.StringVar(window)
color_var.set(colors[0])  # Set the default selected color
color_dropdown = tk.OptionMenu(window, color_var, *colors)
color_dropdown.config(font=("Arial", 14))
color_dropdown.pack()

# Create a button to check the choice
check_button = tk.Button(window, text='Check', command=check_result, font=("Arial", 14))
check_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(window, text="", font=("Arial", 14), fg="blue")
result_label.pack()

# Create labels for player and computer scores
player_score_label = tk.Label(window, text="Player Score: 0", font=("Arial", 14), fg="green")
player_score_label.pack()
computer_score_label = tk.Label(window, text="Computer Score: 0", font=("Arial", 14), fg="red")
computer_score_label.pack()

# Run the main event loop
window.mainloop()
