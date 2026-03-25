class BibliotecaError(Exception):
    """Excepción base para errores de la biblioteca"""

    pass


class LimitePrestamosError(BaseException):
    """Se excedió el límite de préstamos permitidos"""


class TituloInvalidoError(BibliotecaError):
    """El título del libro no es válido"""

    pass


class LibroNoDisponibleError(BibliotecaError):
    """El libro no está disponible para préstamo"""

    pass


class UsuarioNoEncontradoError(BibliotecaError):
    """El usuario no fue encontrado en el sistema"""

    pass
