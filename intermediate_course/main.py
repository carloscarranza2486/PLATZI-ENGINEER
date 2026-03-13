"""
Sistema de análisis de noticias con APIs múltiples.
"""

from news_analyzer.api_client import fetch_news
from news_analyzer.config import API_KEY
from news_analyzer.exceptions import APIKeyError
from news_analyzer.utils import (
    get_unique_sources,
    get_articles_by_source,
    get_reading_time,
)
from news_analyzer.open_ai import analyze_news_with_ia

response_data = None
try:
    response_data = fetch_news("newapi", api_key=API_KEY, query="Python")
except APIKeyError as e:
    print(f"{e}")

if response_data:
    print(analyze_news_with_ia(response_data["articles"], "¿Qué piensas de Python?"))
