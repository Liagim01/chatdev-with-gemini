'''This module contains the BMI calculator class.'''
class BMICalculator:
    def __init__(self):
        pass
    def calculate_bmi(self, height, weight):
        # Convert height to inches
        height_inches = float(height) * 12
        # Calculate BMI
        bmi = float(weight) / (height_inches * height_inches) * 703
        # Return BMI
        return bmi
    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi >= 18.5 and bmi < 25:
            return "Normal weight"
        elif bmi >= 25 and bmi < 30:
            return "Overweight"
        else:
            return "Obese"