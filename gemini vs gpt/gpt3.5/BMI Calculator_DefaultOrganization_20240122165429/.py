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