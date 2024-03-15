'''
This is the main file of the password generator application.
'''
import tkinter as tk
from password_generator import PasswordGenerator
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.password_generator = PasswordGenerator()
        self.password_length_label = tk.Label(root, text="Password Length:")
        self.password_length_label.pack()
        self.password_length_entry = tk.Entry(root)
        self.password_length_entry.pack()
        self.include_lowercase_var = tk.IntVar()
        self.include_lowercase_checkbox = tk.Checkbutton(root, text="Include Lowercase", variable=self.include_lowercase_var)
        self.include_lowercase_checkbox.pack()
        self.include_uppercase_var = tk.IntVar()
        self.include_uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase", variable=self.include_uppercase_var)
        self.include_uppercase_checkbox.pack()
        self.include_numbers_var = tk.IntVar()
        self.include_numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=self.include_numbers_var)
        self.include_numbers_checkbox.pack()
        self.include_symbols_var = tk.IntVar()
        self.include_symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=self.include_symbols_var)
        self.include_symbols_checkbox.pack()
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()
        self.password_label = tk.Label(root, text="")
        self.password_label.pack()
    def generate_password(self):
        password_length = self.password_length_entry.get()
        if not password_length.isdigit() or int(password_length) <= 0:
            # Display an error message or handle the invalid input appropriately
            error_message = "Invalid password length. Please enter a positive integer."
            self.password_label.config(text=error_message)
            return
        password_length = int(password_length)
        include_lowercase = bool(self.include_lowercase_var.get())
        include_uppercase = bool(self.include_uppercase_var.get())
        include_numbers = bool(self.include_numbers_var.get())
        include_symbols = bool(self.include_symbols_var.get())
        password = self.password_generator.generate_password(password_length, include_lowercase, include_uppercase, include_numbers, include_symbols)
        self.password_label.config(text=password)
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()