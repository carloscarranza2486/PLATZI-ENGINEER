def divide(a: int, b: int) -> float:
    # Validar que ambos parámetros sean enteros
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Ambos valores deben ser enteros')
    # Verificamos que el divisor no sea cero
    if b == 0:
        raise ValueError('El divisor no puede ser cero')
    return a/b
# ejemplo de uso
try:
    res = divide(10, 2) # División correcta
    print(res)
except (ValueError, TypeError) as e:
    print(f'Error: {e}')

