import requests
from bs4 import BeautifulSoup

def get_conversation_topics():
  '''
  This function gets conversation topics from the internet.
  '''
  # Get the HTML content of the website.
  url = "https://conversationstarters.com/"
  response = requests.get(url)
  html_content = response.text
  # Parse the HTML content.
  soup = BeautifulSoup(html_content, 'html.parser')
  # Get the conversation topics.
  conversation_topics = []
  for topic in soup.find_all('div', class_='topic'):
    conversation_topics.append(topic.text)
  # Return the conversation topics.
  return conversation_topics