'''This is the main file for the random password generator app.'''
import tkinter as tk
from password_generator import PasswordGenerator
def main():
    window = tk.Tk()
    window.title("Random Password Generator")
    # Create a PasswordGenerator object.
    password_generator = PasswordGenerator()
    # Create a label to display the password.
    password_label = tk.Label(window, text="Password:")
    password_label.grid(row=0, column=0)
    # Create an entry to allow the user to enter the length of the password.
    password_length_entry = tk.Entry(window)
    password_length_entry.grid(row=0, column=1)
    # Create a button to generate a password.
    generate_password_button = tk.Button(window, text="Generate Password", command=lambda: password_generator.generate_password(password_length_entry.get(), password_label))
    generate_password_button.grid(row=1, column=0)
    # Create a button to quit the application.
    quit_button = tk.Button(window, text="Quit", command=window.destroy)
    quit_button.grid(row=1, column=1)
    # Start the main loop.
    window.mainloop()
if __name__ == "__main__":
    main()