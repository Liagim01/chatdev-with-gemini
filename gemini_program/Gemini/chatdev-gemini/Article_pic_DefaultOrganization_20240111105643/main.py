# main.py
import tkinter as tk
from article_processor import ArticleProcessor
class GUI:
    """
    A class to create the graphical user interface for the application.
    """
    def __init__(self):
        """
        The constructor for the GUI class.
        """
        # Create the main window.
        self.window = tk.Tk()
        self.window.title("Article Tool")
        # Create the article processor.
        self.article_processor = ArticleProcessor()
        # Create the text entry widget.
        self.text_entry = tk.Text(self.window)
        self.text_entry.pack()
        # Create the button to process the article.
        self.process_button = tk.Button(self.window, text="Process Article", command=self.process_article)
        self.process_button.pack()
        # Create the text widget to display the markdown.
        self.markdown_display = tk.Text(self.window)
        self.markdown_display.pack()
    def process_article(self):
        """
        Processes the article.
        """
        # Get the text from the text entry widget.
        article_text = self.text_entry.get("1.0", "end")
        # Process the article.
        self.article_processor.process_article(article_text)
        # Get the markdown from the article processor.
        markdown = self.article_processor.get_markdown()
        # Display the markdown in the text widget.
        self.markdown_display.delete("1.0", "end")
        self.markdown_display.insert("1.0", markdown)
    def start(self):
        """
        Starts the main loop of the application.
        """
        self.window.mainloop()
if __name__ == "__main__":
    gui = GUI()
    gui.start()