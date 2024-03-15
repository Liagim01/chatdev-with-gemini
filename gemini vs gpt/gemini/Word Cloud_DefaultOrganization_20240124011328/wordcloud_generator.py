'''This module contains the WordCloudGenerator class, which is responsible for generating word clouds.'''
import matplotlib.pyplot as plt
from wordcloud import WordCloud
class WordCloudGenerator:
    def __init__(self, window):
        self.window = window
        self.text_entry_box = None
    def generate_word_cloud(self):
        # Get the text from the text entry box
        text = self.text_entry_box.get("1.0", "end")
        # Create a WordCloud object
        wordcloud = WordCloud()
        # Generate the word cloud
        wordcloud.generate(text)
        # Display the word cloud
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.show()