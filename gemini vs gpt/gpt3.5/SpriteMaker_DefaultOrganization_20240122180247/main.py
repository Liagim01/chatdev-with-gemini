'''
This is the main file of the pixel art editor application.
'''
import tkinter as tk
from editor import Editor
def main():
    root = tk.Tk()
    editor = Editor(root)
    root.mainloop()
if __name__ == "__main__":
    main()