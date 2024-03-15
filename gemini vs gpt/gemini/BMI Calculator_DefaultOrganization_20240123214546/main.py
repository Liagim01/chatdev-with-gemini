'''This is the main file for the BMI calculator application.'''
import tkinter as tk
from bmi_calculator import BMICalculator
def main():
    window = tk.Tk()
    window.title("BMI Calculator")
    # Create a BMI calculator object
    bmi_calculator = BMICalculator()
    # Create the user interface
    label_height = tk.Label(window, text="Height (in inches):")
    label_height.grid(row=0, column=0)
    entry_height = tk.Entry(window)
    entry_height.grid(row=0, column=1)
    label_weight = tk.Label(window, text="Weight (in pounds):")
    label_weight.grid(row=1, column=0)
    entry_weight = tk.Entry(window)
    entry_weight.grid(row=1, column=1)
    button_calculate = tk.Button(window, text="Calculate BMI", command=lambda: bmi_calculator.calculate_bmi(entry_height.get(), entry_weight.get()))
    button_calculate.grid(row=2, column=1)
    label_result = tk.Label(window, text="BMI:")
    label_result.grid(row=3, column=0)
    entry_result = tk.Entry(window)
    entry_result.grid(row=3, column=1)
    # Start the main loop
    window.mainloop()
if __name__ == "__main__":
    main()