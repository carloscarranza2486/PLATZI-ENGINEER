sample_articles = [
    {'title': 'Python logra nuevo éxito', 'source': {'name': 'TechNews'},
        'description': 'Gran noticia', 'category': 'Tecnología'},
    {'title': 'Mercado en crisis', 'source': {'name': 'Finance'},
        'description': 'Análisis completo', 'category': 'Economía'},
    {'title': 'Nueva tecnología', 'source': {'name': 'TechNews'},
        'description': 'Innovación', 'category': 'Tecnología'},
    {'title': 'Deportes hoy', 'source': {'name': 'Sports'},
        'description': 'Resultados', 'category': 'Deportes'},
    {'title': 'Política actual', 'source': {'name': 'News'},
        'description': 'Actualidad', 'category': 'Política'},
    {'title': 'Ciencia avanza', 'source': {'name': 'Science'},
        'description': 'Descubrimientos', 'category': 'Ciencia'}
]


def extract_titles_traditionales(articles):
    """Extrae solo los títulos usando un bucle for."""
    titles = []
    for article in articles:
        if len(article['title']) > 10:
            titles.append(article['title'])
    return titles


def extract_titles(articles):
    """Extrae solo los títulos usando una comprensión de listas."""
    return [article['title'] for article in articles if len(article['title']) > 10]


def extract_articles_summaries(articles):
    return {article['title']: article['description'] for article in articles if len(article['description']) > 5}

# print(extract_titles_traditionales(sample_articles))
# print()
# print(extract_titles(sample_articles))


print(extract_articles_summaries(sample_articles))
