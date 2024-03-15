'''This is the main file for the digital clock application.'''
import tkinter as tk
from datetime import datetime
def main():
    window = tk.Tk()
    window.title("Digital Clock")
    window.geometry("250x100")
    window.resizable(False, False)
    # Create a label to display the time
    time_label = tk.Label(window, font=("Arial", 50))
    time_label.pack()
    # Update the time every second
    def update_time():
        now = datetime.now()
        time_label.config(text=now.strftime("%I:%M:%S %p"))
        window.after(1000, update_time)
    update_time()
    # Add a button to toggle between 12-hour and 24-hour format
    format_button = tk.Button(window, text="Toggle Format")
    format_button.pack()
    # Define a function to toggle the time format
    def toggle_format():
        if time_label.cget("text")[-2:] == "AM" or time_label.cget("text")[-2:] == "PM":
            time_label.config(text=now.strftime("%H:%M:%S"))
        else:
            time_label.config(text=now.strftime("%I:%M:%S %p"))
    # Bind the button to the toggle_format function
    format_button.config(command=toggle_format)
    window.mainloop()
if __name__ == "__main__":
    main()