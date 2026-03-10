# # main.py - todo el código en un archivo
# """
# Sistema de análisis de noticias co APIs múltiples
# """

# # PEP 8: Configuración centrealizada - constates en MAYÚSCULAS con guines bajos
# API_TIMEOUT = 30
# MAX_RETRIES = 3
# DEFAULT_LANGUAGE = "es"  # PEP 8: Comillas dobles para strings


import urllib.request
import urllib.parse
import json


def clean_text(text: str) -> str:
    """
    Limpia y normaliza una cadena de texto.

    Elimina los espacios en blanco al inicio y al final de la cadena,
    y convierte todos los caracteres a minúsculas. Si la cadena está
    vacía o es None, retorna una cadena vacía sin lanzar excepciones.

    Parámetros
    ----------
    text : str
        La cadena de texto que se desea limpiar y normalizar.
        Puede ser None o una cadena vacía.

    Retorna
    -------
    str
        La cadena de texto sin espacios extremos y en minúsculas.
        Retorna una cadena vacía ("") si la entrada es falsy
        (None, "", espacios, etc.).

    Excepciones
    -----------
    TypeError
        Si ``text`` no es de tipo ``str`` ni ``None``, operaciones como
        ``strip()`` o ``lower()`` lanzarán este error internamente.

    Ejemplos
    --------
    Uso básico con texto normal:

    >>> clean_text("  Hola Mundo  ")
    'hola mundo'

    Texto ya limpio permanece igual:

    >>> clean_text("python")
    'python'

    Cadena vacía retorna cadena vacía:

    >>> clean_text("")
    ''

    Valor None retorna cadena vacía:

    >>> clean_text(None)
    ''

    Texto con caracteres especiales y mayúsculas:

    >>> clean_text("  ÑOÑO  ")
    'ñoño'

    Notas
    -----
    - Esta función **no** elimina espacios internos entre palabras.
    - No realiza normalización Unicode (e.g., acentos o caracteres especiales
      quedan tal como están, solo en minúsculas).
    - Para normalización avanzada, considere usar ``unicodedata.normalize()``.
    """
    if not text:
        return ""
    return text.strip().lower()


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

API_KEY = "302b596673314c03a740f3c64b2f1ff61"
BASE_URL = "https://newsapi.org/v2/everything"


class NewsSystemError(Exception):
    """Error general en la app"""
    pass


class APIKeyError(NewsSystemError):
    """Error cuando la API Key es inválida"""
    pass


def newsapi_client(api_key, query, timeout=30, retries=3):
    query_string = urllib.parse.urlencode({"q": query, "apiKEY": api_key})
    url = f"{BASE_URL}?{query_string}"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
        return f"NewAPI: {query} con timeout {timeout}"
    except urllib.error.HTTPError:
        raise APIKeyError("Ocurrió un error, no se pudo conectar con la API")
        return {"articles": []}


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


response_data = None
try:
    response_data = fetch_news("newapi", api_key=API_KEY, query="Python")
except APIKeyError as e:
    print({e})
if response_data:
    for article in response_data["articles"]:
        print(article["title"])
