'''
This is the main file for the Typing Practice Software. It initializes the application and sets up the main window.
'''
import tkinter as tk
from typing_interface import TypingInterface
def main():
    root = tk.Tk()
    app = TypingInterface(master=root)
    app.mainloop()
if __name__ == '__main__':
    main()