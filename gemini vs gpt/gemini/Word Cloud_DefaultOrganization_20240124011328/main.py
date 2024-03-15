'''This is the main file for the WordCloud application.'''
import tkinter as tk
from wordcloud_generator import WordCloudGenerator
def main():
    window = tk.Tk()
    window.title("WordCloud Generator")
    # Create a WordCloudGenerator object
    wordcloud_generator = WordCloudGenerator(window)
    # Create a text entry box for the user to input text
    text_entry_box = tk.Text(window)
    text_entry_box.pack()
    # Create a button for the user to generate the word cloud
    generate_button = tk.Button(window, text="Generate Word Cloud", command=wordcloud_generator.generate_word_cloud)
    generate_button.pack()
    # Create a label to display the word cloud
    word_cloud_label = tk.Label(window)
    word_cloud_label.pack()
    # Start the main loop
    window.mainloop()
if __name__ == "__main__":
    main()