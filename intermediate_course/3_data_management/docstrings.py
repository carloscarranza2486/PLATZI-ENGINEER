"""
Explicación de docstring.

En esta clase puedo explicar cómo funcionan los docstrings en Python
"""


def ejemplo_sin_docstring():
    return "Hola, Mundo"


def ejemplo_con_docstring() -> str:
    """
    Esta función devuelve un saludo.

    Returns:
        str: Un saludo en español
    """
    return "Hola, Mundo"


# qprint(ejemplo_con_docstring.__doc__)
# help(ejemplo_con_docstring)
print(ejemplo_sin_docstring.__doc__)

# ¿Qué debe incluir el docstring?
"""
Description
Args
Returns
Examples
"""
