'''This is the main file for the pixel art editor.'''
import tkinter as tk
from canvas import Canvas
from toolbar import Toolbar
def main():
    window = tk.Tk()
    window.title("Pixel Art Editor")
    window.geometry("800x600")
    canvas = Canvas(window)
    toolbar = Toolbar(window, canvas)
    window.mainloop()
if __name__ == "__main__":
    main()