'''
This file contains the MarkdownMaker class which is responsible for creating the markdown.
'''
import markdown

class MarkdownMaker:
    def __init__(self, article, image_url):
        self.article = article
        self.image_url = image_url

    def create_markdown(self):
        # Create the markdown for the article
        markdown = f"""
        # {self.article.split(' ')[0]}

        {self.image_url}

        {self.article}
        """
        return markdown