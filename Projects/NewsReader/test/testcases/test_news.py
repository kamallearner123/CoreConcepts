import pytest
import sys
sys.path.append('../..')
from common import read_news

def test_news_reader():
    url = 'https://www.bbc.com/news/world-asia-india-56901739'
    news_reader = NewsReader(url)
    summary = news_reader.get_summary()
    assert len(summary) > 0
    assert summary.startswith('India has recorded more than 300,000 new')
    assert summary.endswith('the country h')