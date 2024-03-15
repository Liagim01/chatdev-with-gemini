'''
This module contains logic to search for and download images based on the article's content using the Unsplash API.
'''
import requests
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
import os
# Download the required NLTK models
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')
class ImageFinder:
    def __init__(self):
        self.api_key = os.getenv('UNSPLASH_API_KEY')
    def find_images_for_article(self, article_text):
        keywords = self.extract_keywords(article_text)
        images = []
        for keyword in keywords:
            image_url = self.search_images(keyword)
            if image_url:
                images.append(image_url)
        return images
    def search_images(self, keyword):
        url = "https://api.unsplash.com/search/photos"
        headers = {
            "Authorization": f"Client-ID {self.api_key}"
        }
        params = {
            "query": keyword,
            "per_page": 1  # Assuming we want only one image per keyword
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            results = response.json()['results']
            if results:
                # Return the first image's URL
                return results[0]['urls']['regular']
            else:
                # No images found for the keyword
                return None
        else:
            # Handle errors (e.g., invalid API key, rate limit exceeded)
            raise Exception(f"Unsplash API error: {response.status_code}")
    def extract_keywords(self, article_text):
        # Tokenize the article into sentences
        sentences = sent_tokenize(article_text)
        # Define a set of stopwords to exclude
        stop_words = set(stopwords.words('english'))
        keywords = set()
        for sentence in sentences:
            # Tokenize the sentence into words and apply part-of-speech tagging
            words = word_tokenize(sentence)
            pos_tags = pos_tag(words)
            # Perform named entity recognition on the tagged words
            named_entities = ne_chunk(pos_tags, binary=True)
            for entity in named_entities:
                # If it's a named entity, add it to the keywords set
                if hasattr(entity, 'label') and entity.label() == 'NE':
                    entity_name = ' '.join(c[0] for c in entity)
                    if entity_name.lower() not in stop_words:
                        keywords.add(entity_name)
        # Return a list of unique keywords
        return list(keywords)