'''
This is the main file of the BMI calculator application.
'''
import tkinter as tk
from tkinter import messagebox
class BMI_Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.label_height = tk.Label(root, text="Height (cm):")
        self.label_height.pack()
        self.entry_height = tk.Entry(root)
        self.entry_height.pack()
        self.label_weight = tk.Label(root, text="Weight (kg):")
        self.label_weight.pack()
        self.entry_weight = tk.Entry(root)
        self.entry_weight.pack()
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate_bmi)
        self.calculate_button.pack()
    def calculate_bmi(self):
        try:
            height = float(self.entry_height.get())
            weight = float(self.entry_weight.get())
            if height <= 0 or weight <= 0:
                raise ValueError("Height and weight must be positive numbers.")
            bmi = weight / ((height/100) ** 2)
            messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
if __name__ == "__main__":
    root = tk.Tk()
    app = BMI_Calculator(root)
    root.mainloop()