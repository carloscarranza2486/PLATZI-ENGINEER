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


def sources_extraction(articles):
    sources = []
    for article in articles:
        if article['source']['name'] not in sources:
            sources.append(article['source']['name'])
    return sources


def sources_extraction_comprehension(articles):
    return {article['source']['name'] for article in articles}


def categorize_traditional(articles):
    sources = sources_extraction_comprehension(articles)
    result = {}

    for source in sources:
        if source not in result:
            result[source] = []

        for article in articles:
            if source == article.get('source').get('name'):
                result[source].append(article)
    return result


print(sources_extraction(sample_articles))
print()
print(categorize_traditional(sample_articles))
