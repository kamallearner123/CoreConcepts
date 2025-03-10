# Create a class which accepts a news article and returns the summary of the article.
# The class should have a method which accepts the news article and returns the summary of the article.

# Class should accept news url, fetch the news article and return the summary of the article.
# It should accpts even key words and return the news articles related to the key words.

import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize

class NewsReader:
    def __init__(self, url):
        self.url = url

    def fetch_news(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        news_article = soup.find_all('p')
        article = ''
        for para in news_article:
            article += para.text
        return article

    def get_summary(self):
        article = self.fetch_news()
        summary = summarize(article, ratio=0.2)
        return summary
