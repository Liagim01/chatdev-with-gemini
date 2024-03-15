import tkinter as tk
from typing_tutor import TypingTutor

def main():
    '''Main function.'''

    # Create the main window.
    root = tk.Tk()
    root.title("Typing Practice")

    # Create the typing tutor.
    typing_tutor = TypingTutor(root)

    # Start the main loop.
    root.mainloop()

if __name__ == "__main__":
    main()