"""
Sistema de análisis de noticias con APIs múltiples.
"""

from news_analyzer.api_client import fetch_news
from news_analyzer.config import API_KEY
from news_analyzer.exceptions import APIKeyError
from news_analyzer.utils import get_unique_sources, get_articles_by_source

response_data = None
try:
    response_data = fetch_news("newapi", api_key=API_KEY, query="Python")
except APIKeyError as e:
    print(f"{e}")

if response_data:
    sources_set = get_unique_sources(response_data["articles"])
    for index, source in enumerate(sources_set, start=1):
        print(f"No: {index} -- {source}")

    # for article in response_data["articles"]:
    #     print(article["title"])

    github_articles = get_articles_by_source(response_data["articles"], "github.com")
    for github_article in github_articles:
        print(github_article["source"]["name"], github_article["title"])
