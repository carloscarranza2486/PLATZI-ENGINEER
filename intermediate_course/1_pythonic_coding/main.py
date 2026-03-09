# # main.py - todo el código en un archivo
# """
# Sistema de análisis de noticias co APIs múltiples
# """

# # PEP 8: Configuración centrealizada - constates en MAYÚSCULAS con guines bajos
# API_TIMEOUT = 30
# MAX_RETRIES = 3
# DEFAULT_LANGUAGE = "es"  # PEP 8: Comillas dobles para strings


# # PEP8: Utilidades comunes del proyecto - funciones en snake_case
# def clean_text(text):
#     # PEP 8: 4 espacios por indentación, no tabs
#     """limpia y normaliza texto."""  # PEP 8: Docstring en comillas dobles triples
#     if not text:
#         return ""
#     return text.strip().lower()


# # PEP 8: Doble línea en blanco entre funciones para separar lógicamente
# def validate_api_key(api_key):
#     """valida que la API key tenga formato correcto."""
#     return (
#         len(api_key) > 10 and api_key.isalnum()
#     )  # PEP 8: Espacios alrededor de operadores


# # PEP 8: Funciones principales - agrupadas después de utilizadas
# def fetch_news_from_api(api_name, query):
#     """Obtiene noticias de una API específica."""
#     pass


# def process_article_data(raw_data):
#     """Procesa datods crudos de artículos."""
#     pass


# # - Longitud de Línea: Máximo 88 caracteres (Ruff default)
# # - Indentación: •4 espacios, • nunca tabs
# # -Nombres descriptivos: snake_case para funciones y variables
# # -Imports• ordenados: estándar•→ terceros •→• locales
# # Líneas en blanco: Separar funciones y clases • lógicamente
# # • Comillas consistentes: Usar comillas dobles para strings

import json
import urllib.parse
import urllib.request


def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f"Guardian {section} desde {from_date} con timeout {timeout}"


def ejemplo_args(api_key, *args):
    print(f"API Key: {api_key}")
    print(f"Args: {args}")
    print(f"type args: {type(args)}")
    print("====")


# ejemplo_args("API_KEY_VALUE", "Este", "parametro", "acá")
# ejemplo_args("API_KEY_VALUE", "Hola", "mundo")


def ejemplo_kwargs(**kwargs):
    print(f"Kwargs: {type(kwargs)}")
    print(f"Kwargs: {kwargs}")
    print("====")


# ejemplo_kwargs(
#     api_key="DEMO",
#     query="Noticias de python",
#     timeout=30,
#     retries=3,
# )
# ejemplo_kwargs(
#     api_key="DEMO GUARDIAN",
#     section="Sports",
#     from_date="2020-10-20",
#     timeout=30,
#     retries=3
# )

API_KEY = "302b596673314c03a740f3c64b2f1ff6"
BASE_URL = "https://newsapi.org/v2/everything"


def newsapi_client(api_key, query, timeout=30, retries=3):
    query_string = urllib.parse.urlencode({"q": query, "apiKEY": api_key})
    url = f"{BASE_URL}?{query_string}"

    with urllib.request.urlopen(url, timeout=timeout) as response:
        data = response.read().decode("utf-8")
        return json.loads(data)
    return f"NewAPI: {query} con timeout {timeout}"


def fetch_news(api_name, *args, **kwargs):
    """
    función flexible para conectar con la API
    """

    base_config = {
        "timeout": 30,
        "retries": 3,
    }

    config = {
        **base_config,
        **kwargs
    }

    api_client = {
        "newapi": newsapi_client,
        "guardian": guardian_client,
    }

    client = api_client[api_name]
    return client(*args, **config)


response_data = fetch_news("newapi", api_key=API_KEY, query="Python")
for article in response_data["articles"]:
    print(article["title"])
