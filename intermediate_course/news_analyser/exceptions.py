"""Definición de excepciones personalizadas para la aplicación."""


class NewsSystemError(Exception):
    """Error general en la app"""

    pass


class APIKeyError(NewsSystemError):
    """Error cuando la API KEY es invalida"""

    pass
