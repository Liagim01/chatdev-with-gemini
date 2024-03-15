'''
Word Cloud Generator
This program generates a word cloud from user input text.
Author: ChatDev
'''
import tkinter as tk
from tkinter import messagebox
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import sys
class WordCloudGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Word Cloud Generator")
        self.text_entry = tk.Text(self.root, height=10, width=50)
        self.text_entry.pack()
        self.generate_button = tk.Button(self.root, text="Generate Word Cloud", command=self.generate_word_cloud)
        self.generate_button.pack()
    def generate_word_cloud(self):
        text = self.text_entry.get("1.0", tk.END)
        if not text.strip():
            messagebox.showerror("Error", "Please enter some text.")
            return
        try:
            wordcloud = WordCloud().generate(text)
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            plt.show()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate word cloud: {e}")
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    word_cloud_generator = WordCloudGenerator()
    word_cloud_generator.run()