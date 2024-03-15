import requests
from bs4 import BeautifulSoup
import markdown
class ArticleProcessor:
    """
    A class to process articles.
    """
    def __init__(self):
        """
        The constructor for the ArticleProcessor class.
        """
        # The URL of the article to be processed.
        self.article_url = None
        # The text of the article.
        self.article_text = None
        # The list of images in the article.
        self.article_images = []
        # The markdown layout of the article.
        self.article_markdown = None
    def process_article(self, article_text):
        """
        Processes the article.
        Args:
            article_text: The text of the article.
        """
        # Set the article text.
        self.article_text = article_text
        # Find the images in the article.
        self.find_images()
        # Create the markdown layout of the article.
        self.create_markdown()
    def find_images(self):
        """
        Finds the images in the article.
        """
        # Create a BeautifulSoup object from the article text.
        soup = BeautifulSoup(self.article_text, "html.parser")
        # Find all the img tags in the article.
        img_tags = soup.find_all("img")
        # Add the src attribute of each img tag to the list of images.
        for img_tag in img_tags:
            self.article_images.append(img_tag["src"])
    def create_markdown(self):
        """
        Creates the markdown layout of the article.
        """
        # Create a markdown string.
        markdown_string = ""
        # Add the title of the article to the markdown string.
        markdown_string += "# " + self.article_text.split("\n")[0] + "\n\n"
        # Add the body of the article to the markdown string.
        markdown_string += self.article_text.split("\n")[1:]
        # Add the images to the markdown string.
        for image in self.article_images:
            markdown_string += "\n\n![Image](" + image + ")\n\n"
        # Set the markdown layout of the article.
        self.article_markdown = markdown_string
    def get_markdown(self):
        """
        Returns the markdown layout of the article.
        Returns:
            The markdown layout of the article.
        """
        return self.article_markdown