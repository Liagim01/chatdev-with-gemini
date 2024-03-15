import re
import os
import requests
from PIL import Image
from PIL import ImageFilter
from bs4 import BeautifulSoup

def main():
  # Get the article content
    article_content = get_article_content()

  # Find all the images in the article
    image_urls =find_images(article_content)

  # Download all the images
    download_images(image_urls)

  # Resize the images
    resize_images()

  # Add the images to the article
    add_images_to_article(article_content, image_urls)

  # Save the article
    save_article(article_content)

def get_article_content():
    with open('article.txt', 'r') as f:
        article_content = f.read()
    return article_content

def find_images(article_content):
    soup = BeautifulSoup(article_content, 'html.parser')
    image_urls = []
    for img in soup.find_all('img'):
        image_urls.append(img['src'])
    return image_urls

def download_images(image_urls):
    for url in image_urls:
        response = requests.get(url)

    with open(os.path.basename(url), 'wb') as f:
        f.write(response.content)

def resize_images():
    for filename in os.listdir('.'):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img = Image.open(filename)
            img = img.resize((500, 500))
            img.save(filename, quality=95)

def add_images_to_article(article_content, image_urls):
    for url in image_urls:
        filename = os.path.basename(url)
        article_content = re.sub(url, '![](' + filename + ')', article_content)
    return article_content

def save_article(article_content):
    with open('article.md', 'w') as f:
        f.write(article_content)

if __name__ == '__main__':
    main()