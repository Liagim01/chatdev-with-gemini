'''This is the main file for the dice rolling simulator.'''
import tkinter as tk
from dice import Dice
def main():
    window = tk.Tk()
    window.title("Dice Rolling Simulator")
    # Create a frame for the dice
    dice_frame = tk.Frame(window)
    dice_frame.pack()
    # Create a label for the number of sides
    num_sides_label = tk.Label(dice_frame, text="Number of sides:")
    num_sides_label.pack(side=tk.LEFT)
    # Create an entry for the number of sides
    num_sides_entry = tk.Entry(dice_frame)
    num_sides_entry.pack(side=tk.LEFT)
    # Create a button to roll the dice
    roll_button = tk.Button(dice_frame, text="Roll", command=lambda: roll_dice(num_sides_entry.get()))
    roll_button.pack(side=tk.LEFT)
    # Create a label for the result
    result_label = tk.Label(dice_frame, text="Result:")
    result_label.pack(side=tk.LEFT)
    # Create a label to display the result
    result_display = tk.Label(dice_frame)
    result_display.pack(side=tk.LEFT)
    # Start the main loop
    window.mainloop()
def roll_dice(num_sides):
    # Create a dice object
    dice = Dice(int(num_sides))
    # Roll the dice
    result = dice.roll()
    # Update the result label
    result_display.config(text=result)
if __name__ == "__main__":
    main()
# dice.py
'''This is a class for a dice.'''
import random
class Dice:
    def __init__(self, num_sides):
        self.num_sides = num_sides
    def roll(self):
        return random.randint(1, self.num_sides)